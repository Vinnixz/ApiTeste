document.getElementById('formulario').addEventListener('submit', async function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    const data = {
        nome: document.getElementById('nome').value,
        email: document.getElementById('email').value
    };
    try {
        console.log(JSON.stringify(data));
        const response = await fetch('http://localhost:8000/teste2', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },

            body: JSON.stringify(data)
        });

        if (response.ok) {
            alert('Dados enviados com sucesso!');
        } else {
            alert('Erro ao enviar dados.');
        }
    } catch (error) {
        console.error('Erro:', error);
    }
});
