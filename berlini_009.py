import sys
import json
import requests

BASE = "https://jsonplaceholder.typicode.com"

def get_posts(user_id):
    resp = requests.get(f"{BASE}/posts", params={"userId": user_id}, timeout=10)
    resp.raise_for_status()
    return resp.json()

def get_comments(post_id):
    resp = requests.get(f"{BASE}/posts/{post_id}/comments", timeout=10)
    resp.raise_for_status()
    return resp.json()

def create_comment(post_id, name, email, body):
    payload = {"postId": post_id, "name": name, "email": email, "body": body}
    resp = requests.post(f"{BASE}/comments", json=payload, timeout=10)
    resp.raise_for_status()
    return resp.json()

def main():
    try:
        posts = get_posts(1)
    except requests.RequestException as e:
        print(f"Errore recupero post: {e}")
        sys.exit(1)

    print("--- Post dell'utente 1 ---")
    if not posts:
        print("Nessun post trovato.")
        return
    for p in posts:
        print(f"ID Post: {p['id']}, Titolo: {p['title']}")

    first_post_id = posts[0]["id"]

    try:
        comments = get_comments(first_post_id)
    except requests.RequestException as e:
        print(f"Errore recupero commenti: {e}")
        sys.exit(1)

    print("\n--- Commenti per il primo post ---")
    for c in comments:
        print(f"- {c['name']}: {c['body']}")

    try:
        new_comment = create_comment(
            first_post_id,
            "Nuovo Commentatore",
            "nuovo@example.com",
            "Questo è un commento aggiunto tramite API!"
        )
    except requests.RequestException as e:
        print(f"Errore creazione commento: {e}")
        sys.exit(1)

    print("\n--- Nuovo Commento Creato ---")
    print(json.dumps(new_comment, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()