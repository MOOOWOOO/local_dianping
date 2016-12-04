/**
 * Created by jux on 16-12-4.
 */

let log = function () {
    console.log(arguments)
}

let api = {}

api.ajax = function (url, method, form, success, error) {
    let req = {
        url: url,
        type: method,
        contentType: "application/json",
        success: function (r) {
            log('ajax success', url, r)
            success(r)
        },
        error: function (err) {
            let r = {
                success: false,
                data: err
            }
            log('ajax err', url, err, error)
            error(r)
        }
    }
    if (method === 'post') {
        let data = JSON.stringify(form)
        req.data = data
    }
    $.ajax(req)
}

api.get = function(url, response) {
    let method = 'get'
    let form = {}
    this.ajax(url, method, form, response, response)
}

api.post = function(url, form, success, error) {
    let method = 'post'
    this.ajax(url, method, form, success, error)
}

