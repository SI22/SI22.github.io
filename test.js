// app.js

// 質問投稿フォームのsubmitイベントを監視し、バリデーションを行う
document.querySelector("#question-form").addEventListener("submit", function(event) {
  // フォームの内容を取得
  const title = document.querySelector("#question-title").value.trim();
  const category = document.querySelector("#question-category").value;
  const content = document.querySelector("#question-content").value.trim();

  // バリデーションのチェック
  if (title.length < 10) {
    alert("質問タイトルは10文字以上で入力してください。");
    event.preventDefault();
    return;
  }

  if (content.length < 30) {
    alert("質問内容は30文字以上で入力してください。");
    event.preventDefault();
    return;
  }

  if (category === "") {
    alert("カテゴリを選択してください。");
    event.preventDefault();
    return;
  }
});

// 質問タイトルの文字数をカウントする
document.querySelector("#question-title").addEventListener("input", function() {
  const title = document.querySelector("#question-title").value.trim();
  const titleCountElement = document.querySelector("#title-count");

  titleCountElement.textContent = title.length;
});
