document.getElementById('assessmentForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const formData = new FormData(this);

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();

        // Display result
        const resultDiv = document.getElementById('result');
        const resultMessage = document.getElementById('resultMessage');

        // Clear any previous classes
        resultDiv.querySelector('.alert').className = 'alert';

        // Add appropriate class and show result
        if (result.prediction === 1) {
            resultDiv.querySelector('.alert').classList.add('alert-danger');
            resultMessage.textContent = 'High Risk: ' + result.message;
        } else {
            resultDiv.querySelector('.alert').classList.add('alert-success');
            resultMessage.textContent = 'Low Risk: ' + result.message;
        }

        resultDiv.style.display = 'block';

        // Scroll to the result
        resultDiv.scrollIntoView({ behavior: 'smooth' });

    } catch (error) {
        console.error('Error:', error);
        const resultDiv = document.getElementById('result');
        const resultMessage = document.getElementById('resultMessage');

        resultDiv.style.display = 'block';
        resultDiv.querySelector('.alert').className = 'alert alert-danger';
        resultMessage.textContent = 'An error occurred while processing your request. Please try again.';
    }
});