const API_URL = import.meta.env.VITE_API_URL
console.log(import.meta.env);
console.log(import.meta.env.VITE_API_URL);

export async function sendMessage(message){
    const response = await fetch(`${API_URL}/chat`,{
        method:"POST",
        headers: {
            "Content-type" : "application/json",

        },
        body: JSON.stringify({
            messages:[
                {
                    role:"user",
                    content:message,
                },
            ],
        }),
    });
    const data = await response.json();
    return data;
}

