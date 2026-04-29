function login() {
    const user = document.getElementById("username").value;
    const pass = document.getElementById("password").value;

    if (user === "admin" && pass === "1234") {
        localStorage.setItem("login", "true");
        window.location.href = "dashboard.html";
    } else {
        alert("Invalid login");
    }
}

function logout() {
    localStorage.removeItem("login");
    window.location.href = "index.html";
}

function addBook() {
    let table = document.getElementById("bookTable");
    let row = table.insertRow();

    row.insertCell(0).innerText = document.getElementById("bookId").value;
    row.insertCell(1).innerText = document.getElementById("title").value;
    row.insertCell(2).innerText = document.getElementById("author").value;
}

function addMember() {
    let table = document.getElementById("memberTable");
    let row = table.insertRow();

    row.insertCell(0).innerText = document.getElementById("memberId").value;
    row.insertCell(1).innerText = document.getElementById("name").value;
}

function issueBook() {
    alert("Book Issued Successfully");
}