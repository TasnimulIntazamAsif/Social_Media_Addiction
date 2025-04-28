document.getElementById('assessmentForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const formData = new FormData(this);

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        // Display result
        const resultDiv = document.getElementById('result');
        const resultMessage = document.getElementById('resultMessage');

        resultDiv.style.display = 'block';
        resultMessage.textContent = result.message;

        // Set appropriate alert class based on prediction
        resultDiv.querySelector('.alert').className = 'alert ' +
            (result.prediction === 1 ? 'alert-danger' : 'alert-success');

    } catch (error) {
        console.error('Error:', error);
        const resultDiv = document.getElementById('result');
        const resultMessage = document.getElementById('resultMessage');

        resultDiv.style.display = 'block';
        resultDiv.querySelector('.alert').className = 'alert alert-danger';
        resultMessage.textContent = 'An error occurred while processing your request. Please try again.';
    }
});