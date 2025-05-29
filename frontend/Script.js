function runCode() {
  const code = document.getElementById('code').value;
  const input = document.getElementById('input').value;

  fetch('http://localhost:5000/run', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({code, input})
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById('output').innerText =
      data.output + (data.errors ? "\nError:\n" + data.errors : "");
  })
  .catch(() => {
    document.getElementById('output').innerText = 'Error connecting to backend';
  });
}
