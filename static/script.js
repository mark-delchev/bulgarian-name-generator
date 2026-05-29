document.getElementsByClassName("generate")[0].onclick = async () => {
            const res = await fetch("/generate", { method: "POST" });
            const data = await res.json();
            document.getElementById("output").innerText = data.name;
        };