<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Тапалка</title>
  <style>
    body {
      text-align: center;
      font-family: sans-serif;
      margin: 0;
      padding: 20px;
      background-color: #f2f2f2;
    }
    h1 {
      font-size: 6vw;
      margin-bottom: 20px;
    }
    #carImage {
      width: 80%;
      max-width: 300px;
      height: auto;
      cursor: pointer;
      transition: transform 0.1s;
    }
    #carImage:active {
      transform: scale(0.97);
    }
    #counter {
      font-size: 5vw;
      margin-top: 20px;
    }

    @media (min-width: 768px) {
      h1 {
        font-size: 32px;
      }
      #counter {
        font-size: 24px;
      }
    }
  </style>
</head>
<body>
  <h1>Тапалка</h1>
  <img id="carImage" src="" alt="Машина">
  <div id="counter">Тапов: 0</div>

  <script>
    let count = parseInt(localStorage.getItem("tapCount")) || 0;
    const image = document.getElementById("carImage");
    const counter = document.getElementById("counter");

    const carImages = [
      "https://grizly.club/uploads/posts/2023-08/1691799404_grizly-club-p-kartinki-zhiguli-bez-fona-9.png", // 0-99
      "https://foni.papik.pro/uploads/posts/2024-10/foni-papik-pro-pk1v-p-kartinki-gelik-na-prozrachnom-fone-2.png", // 100-199
      "", // 200-299
      "", // 300-399
      "", // 400-499
      "", // 500-599
      "", // 600-699
      "", // 700-799
      "", // 800-899
      "" // 900-1000
    ];

    function updateImage() {
      let index = Math.floor(count / 100);
      if (index >= carImages.length) {
        index = carImages.length - 1;
      }
      image.src = carImages[index];
    }

    counter.textContent = `Тапов: ${count}`;
    updateImage();

    image.addEventListener("click", () => {
      count++;
      counter.textContent = `Тапов: ${count}`;
      localStorage.setItem("tapCount", count);
      updateImage();
    });
  </script>
</body>
</html>
