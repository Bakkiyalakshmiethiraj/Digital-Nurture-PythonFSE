export async function getPosts() {

    const response = await fetch(
        "https://jsonplaceholder.typicode.com/posts?_limit=6"
    );

    if (!response.ok) {
        throw new Error("Failed to fetch data");
    }

    return response.json();

}
