document.querySelector('body').addEventListener('mousemove',eyeball);
      function eyeball(){
        const eye = document.querySelectorAll('.eye');
        eye.forEach(function(eye){
          let x = (eye.getBoundingClientRect().left)+(eye.clientWidth / 2);
          let y = (eye.getBoundingClientRect().top)+(eye.clientHeight / 2);

          let radian = Math.atan2(event.pageX - x,event.pageY - y);

          let rotation = (radian * (180/ Math.PI)*-1)+270;
          eye.style.transform = "rotate("+rotation+"deg)"
        })
      }

      let s = document.getElementsByClassName('pre-text');
      for(let i =0;i<s.length;i++){
        s[i].onmouseover = showText;
      }

      function showText(){
        let r = document.getElementById('side-pre');
        r.innerHTML = this.innerHTML;
      }

      // const code = document.querySelectorAll("pre");
      // code.className = 'test';
      
      // code.forEach(codew =>{
      //     codew.classList.add('test');
      // })
      