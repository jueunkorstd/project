
// 현재 시각을 업데이트하는 함수
function updateCurrentTime() {
  var now = new Date();
  var currentTimeElement = document.getElementById("current-time");
  currentTimeElement.textContent =
    now.getFullYear() +
    "-" +
    (now.getMonth() + 1).toString().padStart(2, "0") +
    "-" +
    now.getDate().toString().padStart(2, "0") +
    " " +
    now.getHours().toString().padStart(2, "0") +
    ":" +
    now.getMinutes().toString().padStart(2, "0") +
    ":" +
    now.getSeconds().toString().padStart(2, "0");
}

// 초 단위로 현재 시각 업데이트 실행
setInterval(updateCurrentTime, 1000); // 1000ms = 1초
