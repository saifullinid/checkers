export function getUsername() {
    let loginForm = document.querySelector('.form')
    loginForm.addEventListener('submit', () => {
        let formInputUsername = loginForm.getElementById('username')
        let username = formInputUsername.value

        localStorage.setItem('username', username)
    })
}
