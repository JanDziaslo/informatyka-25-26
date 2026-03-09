import json
import logging
import os
import sys
from typing import Dict, List
from dotenv import load_dotenv

import requests

load_dotenv()  # Załaduj zmienne środowiskowe z .env

# Konfiguracja logowania
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("discord_notify.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)


class DiscordBotClient:
    """Klient Discord Bot API do wysyłania wiadomości z przyciskami."""

    API_BASE = "https://discord.com/api/v10"

    def __init__(self, token: str, channel_id: str):
        """
        Inicjalizacja klienta Discord.

        Args:
            token: Token bota Discord
            channel_id: ID kanału Discord
        """
        self.token = token
        self.channel_id = channel_id
        self.session = requests.Session()
        self.session.headers.update(
            {"Authorization": f"Bot {token}", "Content-Type": "application/json"}
        )

    def send_commit_notification(self, commit_data: Dict) -> bool:
        """
        Wyślij powiadomienie o nowym commicie na Discord.

        Args:
            commit_data: Słownik z danymi commita

        Returns:
            bool: True jeśli wysłanie się powiodło
        """
        try:
            repo_name = commit_data.get("repo_name", "Repozytorium")
            commit_sha = commit_data.get("commit_sha", "")[:7]
            commit_message = commit_data.get("commit_message", "Brak opisu")
            author = commit_data.get("author", "Nieznany")
            branch = commit_data.get("branch", "main")
            repo_url = commit_data.get("repo_url", f"https://github.com/{repo_name}")
            file_changes: Dict[str, Dict[str, int]] = commit_data.get(
                "file_changes", {}
            )
            total_insertions = commit_data.get("insertions", 0)
            total_deletions = commit_data.get("deletions", 0)

            fields = [
                {"name": "📛 Autor", "value": author, "inline": True},
                {"name": "🌿 Gałąź", "value": branch, "inline": True},
                {"name": "🔗 SHA", "value": f"`{commit_sha}`", "inline": True},
            ]

            if file_changes:
                files_list = []
                max_filename_len = (
                    max(len(f) for f in file_changes.keys()) if file_changes else 0
                )

                for filename, stats in list(file_changes.items()):
                    add = stats.get("add", 0)
                    del_count = stats.get("del", 0)

                    if add > 0 and del_count == 0:
                        # Plik zmieniony tylko z dodaniami
                        files_list.append(f"+ {filename:<{max_filename_len}} +{add}")
                    elif add == 0 and del_count > 0:
                        # Plik zmieniony tylko z usunięciami
                        files_list.append(
                            f"- {filename:<{max_filename_len}} -{del_count}"
                        )
                    elif add > 0 or del_count > 0:
                        # Plik zmieniony z dodaniami i usunięciami
                        files_list.append(
                            f"± {filename:<{max_filename_len}} +{add} -{del_count}"
                        )
                    else:
                        # Plik bez zmian (e.g., permissions changed)
                        files_list.append(f"  {filename:<{max_filename_len}} ±")

                files_text = "```diff\n" + "\n".join(files_list) + "\n```"
                if len(file_changes) > 20:
                    files_text += f"\n... i {len(file_changes) - 20} więcej"

                fields.append(
                    {
                        "name": "📁 Zmodyfikowane pliki",
                        "value": files_text,
                        "inline": False,
                    }
                )

            if total_insertions > 0 or total_deletions > 0:
                stats_text = f"+{total_insertions} / -{total_deletions}"
                fields.append(
                    {"name": "📊 Łącznie zmian", "value": stats_text, "inline": True}
                )

            payload = {
                "content": "📦 Nowy commit!",
                "embeds": [
                    {
                        "title": f"Commit na gałęzi {branch}",
                        "description": commit_message[:1000],
                        "color": 5814783,
                        "fields": fields,
                        "footer": {"text": repo_name},
                    }
                ],
                "components": [
                    {
                        "type": 1,
                        "components": [
                            {
                                "type": 2,
                                "style": 5,
                                "label": "🔗 Zobacz w repozytorium",
                                "url": repo_url,
                            },
                        ],
                    }
                ],
            }

            url = f"{self.API_BASE}/channels/{self.channel_id}/messages"
            response = self.session.post(url, json=payload, timeout=10)

            if response.status_code == 200:
                logger.info(f"✓ Wysłano powiadomienie o commicie {commit_sha}")
                return True
            else:
                logger.error(
                    f"✗ Błąd Discord API {response.status_code}: {response.text}"
                )
                return False

        except Exception as e:
            logger.error(f"✗ Błąd podczas wysyłania powiadomienia: {e}")
            return False


def main() -> int:
    """
    Główna funkcja skryptu - wysyła powiadomienie o commicie.

    Returns:
        int: Kod wyjścia (0 = sukces, 1 = błąd)
    """
    bot_token = os.getenv("DISCORD_BOT_TOKEN")
    channel_id = os.getenv("DISCORD_CHANNEL_ID")

    if not bot_token or not channel_id:
        logger.warning("⚠ Brak DISCORD_BOT_TOKEN lub DISCORD_CHANNEL_ID")
        logger.warning("Wysyłanie powiadomień na Discord jest wyłączone")
        return 0

    repo_name = os.getenv("GITHUB_REPOSITORY", "JanDziaslo/informatyka-25-26")
    commit_sha = os.getenv("GITHUB_SHA", "")
    author = os.getenv("GITHUB_ACTOR", "Nieznany")
    commit_message = os.getenv("COMMIT_MESSAGE", "Brak opisu commita")
    branch = os.getenv("GITHUB_REF", "refs/heads/main").replace("refs/heads/", "")
    repo_url = f"https://github.com/{repo_name}"

    modified_files_raw = os.getenv("MODIFIED_FILES_JSON", "")
    try:
        if not modified_files_raw or modified_files_raw in ("null", "None", ""):
            file_changes = {}
        else:
            file_changes = {}
            for entry in modified_files_raw.split("|"):
                if entry:
                    parts = entry.split(":")
                    if len(parts) == 3:
                        filename, add, del_count = parts
                        file_changes[filename] = {
                            "add": int(add),
                            "del": int(del_count),
                        }
    except (ValueError, json.JSONDecodeError):
        file_changes = {}

    try:
        insertions = int(os.getenv("COMMIT_INSERTIONS", "0"))
        deletions = int(os.getenv("COMMIT_DELETIONS", "0"))
    except ValueError:
        insertions = 0
        deletions = 0

    logger.info("=" * 60)
    logger.info("🤖 Wysyłanie powiadomienia o commicie na Discord")
    logger.info(f"Repo: {repo_name}")
    logger.info(f"Commit: {commit_sha[:7]}")
    logger.info(f"Autor: {author}")
    logger.info(f"Pliki: {len(file_changes)}")
    logger.info(f"Zmiany: +{insertions} / -{deletions}")
    logger.info("=" * 60)

    commit_data = {
        "repo_name": repo_name,
        "commit_sha": commit_sha,
        "commit_message": commit_message,
        "author": author,
        "branch": branch,
        "repo_url": repo_url,
        "file_changes": file_changes,
        "insertions": insertions,
        "deletions": deletions,
    }

    client = DiscordBotClient(bot_token, channel_id)
    if client.send_commit_notification(commit_data):
        logger.info("✓ Skrypt zakończony sukcesem")
        logger.info("=" * 60)
        return 0
    else:
        logger.error("✗ Nie udało się wysłać powiadomienia")
        logger.info("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
