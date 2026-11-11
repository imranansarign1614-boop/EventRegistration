document.getElementById("registrationForm")
.addEventListener("submit", function(event) {

    event.preventDefault();

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let phone = document.getElementById("phone").value;
    let eventName = document.getElementById("event").value;

    alert("Registration Successful!\n" +
          "Name: " + name + "\n" +
          "Email: " + email + "\n" +
          "Event: " + eventName);
});