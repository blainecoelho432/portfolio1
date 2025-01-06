<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blaine's Portfolio</title>

    <!-- Internal CSS -->

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <link href="<link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bungee+Tint&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #000000;
            color: #000000;A
        }

        header {
            background-color: #000000;
            color: rgb(0, 0, 0);
            padding: 10px 0;
            text-align: center;
        }

        header h1 {
            margin: 0;
            font-size: 2.5em;
            font-family: 'Roboto', sans-serif;
        }
        </style>
        <style>
        body,
        html {
            margin: 0;
            padding: 0;
            font-family: sans-serif;
            font-size: 20px;
            color: #000000;
        }

        a {
            color: inherit;
        }

        .page {
            width: 100%;
            min-height: 180vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            opacity: 0;
        }

        .page .header {
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 40px;
            text-transform: uppercase;
            width: 100vw;
            margin-top: 20vh;
            height: 25vh;
        }

        .page .content {
            max-width: 800px;
            padding: 10px;
        }

        .page .last-line {
            text-align: right;
            padding-top: 1em;
        }

        .page ::-moz-selection {
            background: #000000;
        }

        .page ::selection {
            background: #000000;
        }

        .scroll-msg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            pointer-events: none;
            padding-top: 2em;
        }

        .scroll-msg>div:nth-child(1) {
            margin-top: -10vh;
            padding-bottom: 1em;
            text-transform: uppercase;
            font-size: 2em;
        }

        canvas#fire-overlay {
            position: fixed;
            top: 0;
            left: 0;
            display: block;
            width: 100%;
            pointer-events: none;
        }

        .arrow-animated {
            font-size: 1em;
            animation: arrow-float 1s infinite;
        }

        @keyframes arrow-float {
            0% {
                transform: translateY(0);
                animation-timing-function: ease-out;
            }

            60% {
                transform: translateY(50%);
                animation-timing-function: ease-in-out;
            }

            100% {
                transform: translateY(0);
                animation-timing-function: ease-out;
            }
        }

        /* Additional CSS for the image */
        .content img {
            width: 100%;
            height: auto;
            margin-bottom: 20px;
            border-radius: 10px;
        }
    </style>
</head>

<body>
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Background Music</title>
      <style>
          /* Simple styling for the overlay */
          #overlay {
              position: fixed;
              top: 0;
              left: 0;
              width: 100%;
              height: 100%;
              background-color: rgba(0, 0, 0, 0.8);
              color: white;
              display: flex;
              justify-content: center;
              align-items: center;
              font-size: 24px;
              z-index: 1000;
              cursor: pointer;
          }
      </style>
  </head>
  <body>
      <!-- Background music -->
      <audio id="backgroundMusic" loop>
          <source src="ark-patrol-slowed-to-perfection-ghostlycheeks-edited123.mp3" type="audio/mpeg">
          Your browser does not support the audio element.
      </audio>
  
      <!-- Click overlay -->
      <div id="overlay">
          Click to Start
      </div>
  
      <script>
          var overlay = document.getElementById('overlay');
          overlay.addEventListener('click', function() {
              var audio = document.getElementById('backgroundMusic');
              audio.play();
              overlay.style.display = 'none';
          })
  
  </script>
    <!-- HTML Content -->
    <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>This is my Portfolio</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: rgb(0, 0, 0);
                color: #000000;
            }
    
            header {
                background-color: #000000;
                color: rgb(0, 0, 0);
                padding: 10px 0;
                text-align: center;
            }
    
            header h1 {
                margin: 0;
                font-size: 2.5em;
            }
    
            nav {
                display: flex;
                justify-content: center;
                padding: 10px;
                background-color: #000000;
            }
    
            nav a {
                color: rgb(0, 0, 0);
                text-decoration: none;
                padding: 0 15px;
                font-weight: bold;
            }
    
            nav a:hover {
                text-decoration: underline;
            }
    
            section {
                padding: 20px;
                max-width: 900px;
                margin: auto;
            }
    
            .about, .projects, .contact {
                margin-bottom: 40px;
            }
    
            h2 {
                font-size: 2em;
                border-bottom: 2px solid #000000;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }
    
            .project {
                display: flex;
                flex-wrap: wrap;
                margin-bottom: 20px;
            }
    
            .project img {
                max-width: 100%;
                margin-right: 20px;
                height: auto;
            }
    
            .project-info {
                max-width: 500px;
            }
    
            footer {
                background-color: #333;
                color: rgb(255, 255, 255);
                text-align: center;
                padding: 20px 0;
                margin-top: 20px;
            }
    
            @media (max-width: 600px) {
                .project {
                    flex-direction: column;
                }
    
                .project img {
                    margin: 0 0 20px 0;
                }
            }
        </style>
    </head>
    <body>
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Image with Blended Clickable Buttons</title>
          <style>
              /* Container for the image and buttons */
              .image-container {
                  position: relative;
                  width: 100%;
                  max-width: 1366px; /* Adjust the width as needed */
                  margin: 0 auto; /* Center the container */
              }
      
              /* The image itself */
              .image-container img {
                  width: 100%; /* Make the image responsive */
                  height: auto;
              }
      
              /* Style for the buttons */
              .button {
                  position: absolute; /* Position the buttons over the image */
                  padding: 10px 20px;
                  background-color: rgba(255, 255, 255, 0.3); /* Semi-transparent white */
                  color: #fff;
                  border: 2px solid rgba(255, 255, 255, 0.5); /* Semi-transparent white border */
                  cursor: pointer;
                  font-size: 16px;
                  border-radius: 10px;
                  text-align: center;
                  text-decoration: none;
                  transition: background-color 0.3s, border 0.3s; /* Smooth transition for hover effect */
              }
      
              /* Button hover effect */
              .button:hover {
                  background-color: rgba(255, 255, 255, 0.5); /* Slightly more opaque on hover */
                  border-color: rgba(255, 255, 255, 0.8); /* More opaque border on hover */
              }
      
              /* Positioning the buttons */
              .button1 {
                  top: 42%;
                  left: 80%;
              }
      
              .button2 {
                  top: 60%;
                  left: 80%;
                  transform: translate(-50%, -50%);
              }
      
              .button3 {
                  bottom: 23%;
                  right: 35%;
              }
          </style>
      </head>
      <body>
          <div class="image-container">
              <img src="BLAINE COELHO.png" alt="Background Image">
              
              <!-- Buttons positioned over the image -->
              <a href="#" class="button button1">🔴</a>
              <a href="#" class="button button2">🔴</a>
              <a href="https://www.instagram.com/ayoblaine?igsh=ZnV3dGN6Z3J2MTRl" class="button button3">🔴</a>
          </div>
      </body>
      <center><img src="BLAINE COELHO 2.png" alt="Background Image"></center>
    
        <center><img src="3.png" alt="Background Image"></center>
        <footer>
            <p>&copy; 2024 My Portfolio. All rights reserved.</p>
        </footer>    

    <canvas id="fire-overlay"></canvas>
    <div class="scroll-msg">
        <div>Hello 👋</div>
        <div>you should scroll ;)</div>
        <div class="arrow-animated">&darr;</div>
    </div>

    <!-- Shader Scripts -->
    <script type="x-shader/x-fragment" id="vertShader">
        precision mediump float;

        varying vec2 vUv;
        attribute vec2 a_position;

        void main() {
            vUv = a_position;
            gl_Position = vec4(a_position, 0.0, 1.0);
        }
    </script>

    <script type="x-shader/x-fragment" id="fragShader">
        precision mediump float;

        varying vec2 vUv;
        uniform vec2 u_resolution;
        uniform float u_progress;
        uniform float u_time;

        float rand(vec2 n) {
            return fract(cos(dot(n, vec2(12.9898, 4.1414))) * 43758.5453);
        }

        float noise(vec2 n) {
            const vec2 d = vec2(0., 1.);
            vec2 b = floor(n), f = smoothstep(vec2(0.0), vec2(1.0), fract(n));
            return mix(mix(rand(b), rand(b + d.yx), f.x), mix(rand(b + d.xy), rand(b + d.yy), f.x), f.y);
        }

        float fbm(vec2 n) {
            float total = 0.0, amplitude = .4;
            for (int i = 0; i < 4; i++) {
                total += noise(n) * amplitude;
                n += n;
                amplitude *= 0.6;
            }
            return total;
        }

        void main() {
            vec2 uv = vUv;
            uv.x *= min(1., u_resolution.x / u_resolution.y);
            uv.y *= min(1., u_resolution.y / u_resolution.x);

            float t = u_progress;
            vec3 color = vec3(1., 1., .95);

            float main_noise = 1. - fbm(.75 * uv + 10. - vec2(.3, .9 * t));

            float paper_darkness = smoothstep(main_noise - .1, main_noise, t);
            color -= vec3(.99, .95, .99) * paper_darkness;

            vec3 fire_color = fbm(6. * uv - vec2(0., .005 * u_time)) * vec3(6., 1.4, .0);
            float show_fire = smoothstep(.4, .9, fbm(10. * uv + 2. - vec2(0., .005 * u_time)));
            show_fire += smoothstep(.7, .8, fbm(.5 * uv + 5. - vec2(0., .001 * u_time)));

            float fire_border = .02 * show_fire;
            float fire_edge = smoothstep(main_noise - fire_border, main_noise - .5 * fire_border, t);
            fire_edge *= (1. - smoothstep(main_noise - .5 * fire_border, main_noise, t));
            color += fire_color * fire_edge;

            float opacity = 1. - smoothstep(main_noise - .0005, main_noise, t);

            gl_FragColor = vec4(color, opacity);
        }
    </script>

    <!-- External JS -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.7.1/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.7.1/ScrollTrigger.min.js"></script>

    <!-- Main JavaScript -->
    <script>
        const canvasEl = document.querySelector("#fire-overlay");
        const scrollMsgEl = document.querySelector(".scroll-msg");

        const params = {
            fireTime: .35,
            fireTimeAddition: 0
        }

        let st, uniforms;
        const gl = initShader();

        st = gsap.timeline({
            scrollTrigger: {
                trigger: ".page",
                start: "0% 0%",
                end: "100% 100%",
                scrub: true,
                onLeaveBack: () => {},
            },
        })
            .to(scrollMsgEl, {
                duration: .1,
                opacity: 0
            }, 0)
            .to(params, {
                fireTime: .63
            }, 0)

        window.addEventListener("resize", resizeCanvas);
        resizeCanvas();

        gsap.set(".page", {
            opacity: 1
        })

        function initShader() {
            const vsSource = document.getElementById("vertShader").innerHTML;
            const fsSource = document.getElementById("fragShader").innerHTML;

            const gl = canvasEl.getContext("webgl") || canvasEl.getContext("experimental-webgl");

            if (!gl) {
                alert("WebGL is not supported by your browser.");
            }

            function createShader(gl, sourceCode, type) {
                const shader = gl.createShader(type);
                gl.shaderSource(shader, sourceCode);
                gl.compileShader(shader);

                if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
                    console.error("An error occurred compiling the shaders: " + gl.getShaderInfoLog(shader));
                    gl.deleteShader(shader);
                    return null;
                }

                return shader;
            }

            const vertexShader = createShader(gl, vsSource, gl.VERTEX_SHADER);
            const fragmentShader = createShader(gl, fsSource, gl.FRAGMENT_SHADER);

            function createShaderProgram(gl, vertexShader, fragmentShader) {
                const program = gl.createProgram();
                gl.attachShader(program, vertexShader);
                gl.attachShader(program, fragmentShader);
                gl.linkProgram(program);

                if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
                    console.error("Unable to initialize the shader program: " + gl.getProgramInfoLog(program));
                    return null;
                }

                return program;
            }

            const shaderProgram = createShaderProgram(gl, vertexShader, fragmentShader);
            uniforms = getUniforms(shaderProgram);

            function getUniforms(program) {
                let uniforms = [];
                let uniformCount = gl.getProgramParameter(program, gl.ACTIVE_UNIFORMS);
                for (let i = 0; i < uniformCount; i++) {
                    let uniformName = gl.getActiveUniform(program, i).name;
                    uniforms[uniformName] = gl.getUniformLocation(program, uniformName);
                }
                return uniforms;
            }

            const vertices = new Float32Array([-1., -1., 1., -1., -1., 1., 1., 1.]);

            const vertexBuffer = gl.createBuffer();
            gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
            gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);

            gl.useProgram(shaderProgram);

            const positionLocation = gl.getAttribLocation(shaderProgram, "a_position");
            gl.enableVertexAttribArray(positionLocation);

            gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
            gl.vertexAttribPointer(positionLocation, 2, gl.FLOAT, false, 0, 0);

            return gl;
        }

        function render() {
            const currentTime = performance.now();
            gl.uniform1f(uniforms.u_time, currentTime);

            gl.uniform1f(uniforms.u_progress, params.fireTime + params.fireTimeAddition);
            gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);

            requestAnimationFrame(render);
        }

        function resizeCanvas() {
            canvasEl.width = window.innerWidth * devicePixelRatio;
            canvasEl.height = window.innerHeight * devicePixelRatio;
            gl.viewport(0, 0, canvasEl.width, canvasEl.height);
            gl.uniform2f(uniforms.u_resolution, canvasEl.width, canvasEl.height);
            render();
        }
    </script>
</body>

</html>
