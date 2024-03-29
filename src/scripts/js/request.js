export const delay = options => {
    return new Promise(function (resolve, reject) {
        if (options.params) {
            options.method = 'POST'
        } else {
            options.method = 'GET'
        }
        let timeout = 1000
        if (options.method === 'POST') {
            timeout = 500
        }
        var xhr = new XMLHttpRequest()
        xhr.open(options.method, options.url)
        xhr.responseType = 'json'
        xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status <= 300) {
            resolve(xhr.response)
        } else {
            reject({
            status: xhr.status,
            statusText: xhr.statusText
            })
        }
        }
        xhr.onerror = function () {
        reject({
            status: xhr.status,
            statusText: xhr.statusText
        })
        }
        if (options.headers) {
            Object.keys(options.headers).forEach(function (key) {
                xhr.setRequestHeader(key, options.headers[key])
            })
        }
        var params = JSON.stringify(options.params)
        setTimeout(() => {
            xhr.send(params)
        }, timeout)
      })
}
