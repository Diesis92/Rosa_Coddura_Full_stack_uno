var funcs = [];
        for (var i = 0; i < 4; i++) {
            funcs.push(function() {
               return i;
            });
        }
        funcs.forEach(function(f) {
            console.log(f());
        }); // 4 4 4 4

        // Soluzione 1: let
        var funcs = [];
        for (let i = 0; i < 4; i++) {
            funcs.push(function() {
               return i;
            });
        }
        funcs.forEach(function(f) {
            console.log(f());
        }); // 0 1 2 3
    //early binding
        var funcs = [];
        for (var i = 0; i < 4; i++) {
            funcs.push((function(x) {
                return function() {
                    return x;
                }
            })(i));
        }
        funcs.forEach(function(f) {
            console.log(f());
        }); // 0 1 2 3