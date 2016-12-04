/**
 * Created by jux on 16-12-4.
 */

let ping_form = {}

ping_form.send = function (url, form, response) {
    let data = JSON.stringify(form)
    console.log('send data', data)
    $.ajax({
        url: url,
        type: 'post',
        data: data,
        contentType: 'application/json',
        success: function (r) {
            response(r)
        },
        error: function (err) {
            let r = {
                success: false,
                message: err,
            }
            response(r)
        }
    })
}

