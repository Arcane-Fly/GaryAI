from github import Github
from code_analyzer import CodeAnalyzer
from llm import LLM

def main():
    # Access Github account and associated organisation
    github = Github("https://github.com/GaryOcean428", "https://github.com/Arcane-Fly")
    
    # Create or update "GaryAI" repo
    repo = github.create_or_update_repo("GaryAI")
    
    # Analyze other projects
    projects = ["KevinAI", "SuperAGI"]
    for project in projects:
        github.analyze_project(project)
    
    # Extract and optimize code blocks
    analyzer = CodeAnalyzer()
    analyzer.extract_and_optimize_code_blocks(github)
    
    # Use various LLMs
    llm = LLM()
    llm.use_llms(analyzer)
    
    # Communicate progress
    with open("progress_notes.txt", "w") as f:
        f.write("Progress: {}\n".format(analyzer.progress))
    
    # Update deployment notes
    with open("deployment_notes.txt", "w") as f:
        f.write("Deployment: {}\n".format(llm.deployment))

if __name__ == "__main__":
    main()
