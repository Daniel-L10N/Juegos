(function() {
    window.onload = function() {
      var runningTotal;
      var buttons = Array.prototype.slice.call(document.querySelectorAll('button'));
  
      var handleComputation = function(event){
        var value = event.currentTarget.textContent;
        var output = document.querySelector('.output')
        if(value === '='){
          runningTotal = eval(runningTotal);
          output.innerHTML = runningTotal;
          return;
        }
        else if(value === 'clear'){
          runningTotal = null;
          output.innerHTML = 'Clearing the screen...';
          setTimeout(function() {
            output.innerHTML = '';
          }, 1000);
          return;
        }
        else if(value === '+' || value === '/' || value === '*' || value === '-'){
          runningTotal += value;
          output.innerHTML = runningTotal;
          return
        }
        else {
          runningTotal = output.innerHTML + value;
          output.innerHTML += value;
          return;
        }
      };
  
      buttons.forEach(function(button) {
        button.addEventListener('click', handleComputation, false);
      });
    }
  }());