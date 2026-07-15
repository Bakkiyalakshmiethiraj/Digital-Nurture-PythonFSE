    const container = document.getElementById("notificationContainer");
    const loading = document.getElementById("loading");

    document.getElementById("loadBtn").addEventListener("click", loadNotifications);

    document.getElementById("retryBtn").addEventListener("click", loadNotifications);

    async function loadNotifications(){

        loading.textContent = "Loading notifications...";

        container.innerHTML = "";

        try{

            const response = await fetch("https://jsonplaceholder.typicode.com/posts?_limit=5");

            if(!response.ok){

                throw new Error("Unable to fetch data.");

            }

            const data = await response.json();

            loading.textContent = "";

            data.forEach(post=>{

                const card = document.createElement("div");

                card.className = "notification-card";

                card.innerHTML=`

                    <h3>${post.title}</h3>

                    <p>${post.body}</p>

                `;

                container.appendChild(card);

            });

        }

        catch(error){

            loading.textContent="";

            container.innerHTML=`
                <p style="color:red;">
                    ${error.message}
                </p>
            `;

        }

    }