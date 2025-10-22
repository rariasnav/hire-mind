import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

def load_github_repos(
    repos: list[str],
    file_extensions: list[str] = [".py", ".js", ".ts", ".tsx", ".md", ".html", ".css", ".json"]
) -> list[str]:
    """
    Load the content of relevant files from multiple Github repositories.
    Returns a list of strings, each representing the content of a file.
    """
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError(" GITHUB_TOKEN not found in .env file")
    
    g = Github(token)
    all_texts = []
    
    for repo_name in repos:
        try:
            repo = g.get_repo(repo_name)
            contents = repo.get_contents("")
            
            while contents:
                file_content = contents.pop(0)
                if file_content.type == "dir":
                    contents.extend(repo.get_contents(file_content.path))
                elif any(file_content.path.endswith(ext) for ext in file_extensions):
                    try:
                        decoded = file_content.decoded_content.decode("utf-8", errors="ignore")
                        all_texts.append(decoded)
                    except Exception as e:
                        print(f"⚠️ Couldn't read {file_content.path}: {e}")
            print(f"Total files loaded from{repo_name}: {len(all_texts)}")
        except Exception as e:
            print(f"❌ Error loading {repo_name}: {e}")
            
    return all_texts