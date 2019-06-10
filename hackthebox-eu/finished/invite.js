eval(
  function (p, a, c, k, e, d) {
    e = function (c) {
        return c.toString(36) // => `o`
    };
    if (!''.replace(/^/, String)) { // true
        while (c--) {
            d[c.toString(a)] = k[c] || c.toString(a)
        }
        k = [function (e) {
            return d[e]
        }];
        e = function () {
            return '\\w+'
        };
        c = 1
    };
    while (c--) {
        if (k[c]) {
            p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c])
        }
    }
    return p
}
  ('1 i(4){h 8={"4":4};$.9({a:"7",5:"6",g:8,b:\'/d/e/n\',c:1(0){3.2(0)},f:1(0){3.2(0)}})}1 j(){$.9({a:"7",5:"6",b:\'/d/e/k/l/m\',c:1(0){3.2(0)},f:1(0){3.2(0)}})}',
   24,
   24,
   'response|function|log|console|code|dataType|json|POST|formData|ajax|type|url|success|api|invite|error|data|var|verifyInviteCode|makeInviteCode|how|to|generate|verify'.split('|'),
   0,
   {}));

// results in
function verifyInviteCode(code){var formData={"code":code};$.ajax({type:"POST",dataType:"json",data:formData,url:'/api/invite/verify',success:function(response){console.log(response)},error:function(response){console.log(response)}})}function makeInviteCode(){$.ajax({type:"POST",dataType:"json",url:'/api/invite/how/to/generate',success:function(response){console.log(response)},error:function(response){console.log(response)}})}

// =>
function verifyInviteCode(code) {
    var formData = {
        "code": code
    };
    $.ajax({
        type: "POST",
        dataType: "json",
        data: formData,
        url: '/api/invite/verify',
        success: function (response) {
            console.log(response)
        },
        error: function (response) {
            console.log(response)
        }
    })
}

function makeInviteCode() {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: '/api/invite/how/to/generate',
        success: function (response) {
            console.log(response)
        },
        error: function (response) {
            console.log(response)
        }
    })
}

// calling `makeInviteCode` returns a string either in base64 or rot13 (maybe more)
// decrypted it says:
// "In order to generate the invite code, make a POST request to /api/invite/generate"
//
// calling `$.post('/api/invite/generate');` in the cli fetches the responseText
// containing the invide code.
$.post('/api/invite/generate', success = function(res) { console.log(res.data);});
// gives:
// {code: "WERYVUEtS1NNT1EtSkdPVVctWkNLTVEtUldWRUg=", format: "encoded"}
//
// and finally:
// > echo "WERYVUEtS1NNT1EtSkdPVVctWkNLTVEtUldWRUg=" | base64 -D
