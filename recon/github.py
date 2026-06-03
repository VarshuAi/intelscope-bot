import requests

def lookup_github(username):
    """
    Queries public GitHub API to extract user profile statistics and details.
    """
    cleaned_user = username.strip().replace("@", "")
    if not cleaned_user:
        return {"status": "error", "message": "Invalid GitHub username format."}
        
    url = f"https://api.github.com/users/{cleaned_user}"
    
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 404:
            return {"status": "error", "message": "GitHub user profile not found."}
        elif response.status_code != 200:
            return {"status": "error", "message": f"GitHub API returned error code {response.status_code}"}
            
        data = response.json()
        
        return {
            "status": "success",
            "username": data.get("login"),
            "name": data.get("name") or "No Name Provided",
            "bio": data.get("bio") or "No biography available.",
            "public_repos": data.get("public_repos", 0),
            "gists": data.get("public_gists", 0),
            "followers": data.get("followers", 0),
            "following": data.get("following", 0),
            "location": data.get("location") or "Not Specified",
            "blog": data.get("blog") or "None",
            "company": data.get("company") or "None",
            "created_at": data.get("created_at", "Unknown").split("T")[0],
            "html_url": data.get("html_url")
        }
    except Exception as e:
        return {"status": "error", "message": f"Connection failed: {str(e)}"}
