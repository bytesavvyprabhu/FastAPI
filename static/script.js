/ script.js

// LogIN pop-up
const showLoginPopupButton = document.getElementById("showLoginPopup");
const loginPopup = document.getElementById("loginPopup");
const closeLoginPopupButton = document.getElementById("closeLoginPopup");
const loginSubmitButton = document.getElementById("loginSubmit");
const loginEmailInput = document.getElementById("loginEmailInput");
const loginPasswordInput = document.getElementById("loginPasswordInput");

showLoginPopupButton.addEventListener("click", function() {
    loginPopup.style.display = "block";
});

closeLoginPopupButton.addEventListener("click", function() {
    loginPopup.style.display = "none";
});

loginSubmitButton.addEventListener("click", function() {
    const email = loginEmailInput.value;
    const password = loginPasswordInput.value;
    // Handle login logic here
    // Example: You might want to make an AJAX request to your FastAPI endpoint.
    loginPopup.style.display = "none";
});

// SignUP pop-up
const showSignupPopupButton = document.getElementById("showSignupPopup");
const signupPopup = document.getElementById("signupPopup");
const closeSignupPopupButton = document.getElementById("closeSignupPopup");
const signupSubmitButton = document.getElementById("signupSubmit");
const signupNameInput = document.getElementById("signupNameInput");
const signupEmailInput = document.getElementById("signupEmailInput");
const signupPasswordInput = document.getElementById("signupPasswordInput");

showSignupPopupButton.addEventListener("click", function() {
    signupPopup.style.display = "block";
});

closeSignupPopupButton.addEventListener("click", function() {
    signupPopup.style.display = "none";
});

signupSubmitButton.addEventListener("click", function() {
    const name = signupNameInput.value;
    const email = signupEmailInput.value;
    const password = signupPasswordInput.value;
    // Handle signup logic here
    // Example: You might want to make an AJAX request to your FastAPI endpoint.
    signupPopup.style.display = "none";
});