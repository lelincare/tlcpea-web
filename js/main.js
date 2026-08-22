// 社團法人臺南市長期照顧職能培力協會 — 共用互動邏輯

document.addEventListener('DOMContentLoaded', () => {
  // 行動版選單開關
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', () => {
      const open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => links.classList.remove('open'));
    });
  }

  // 滾動顯現動畫
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });
    revealEls.forEach(el => io.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add('in'));
  }

  // 課程篩選頁籤（courses.html）
  const tabs = document.querySelectorAll('.filter-tabs button');
  const cards = document.querySelectorAll('[data-track]');
  if (tabs.length && cards.length) {
    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        const track = tab.getAttribute('data-filter');
        cards.forEach(card => {
          const match = track === 'all' || card.getAttribute('data-track') === track;
          card.style.display = match ? '' : 'none';
        });
      });
    });
  }

  // 通用：以 AJAX 方式送出表單到 Netlify Forms
  function submitToNetlify(form, successText, failText, resetDelay) {
    const btn = form.querySelector('button[type="submit"]');
    const original = btn.textContent;
    btn.disabled = true;
    btn.textContent = '送出中…';

    const body = new URLSearchParams(new FormData(form)).toString();

    fetch('/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: body
    })
      .then((res) => {
        if (!res.ok) throw new Error('submit failed: ' + res.status);
        btn.textContent = successText;
        form.reset();
        setTimeout(() => { btn.textContent = original; btn.disabled = false; }, resetDelay);
      })
      .catch(() => {
        btn.textContent = failText;
        btn.disabled = false;
        setTimeout(() => { btn.textContent = original; }, resetDelay);
      });
  }

  // 聯絡表單（Netlify Forms）
  const contactForm = document.querySelector('#contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      submitToNetlify(contactForm, '已收到，感謝您的訊息', '送出失敗，請稍後再試或改用電話聯絡', 2600);
    });
  }

  // 入會表單：依會員類別顯示／隱藏團體／贊助專用欄位
  const memberTypeSelect = document.querySelector('#member-type');
  const groupOnlyFields = document.querySelectorAll('.group-only-field');
  const sponsorOnlyFields = document.querySelectorAll('.sponsor-only-field');
  if (memberTypeSelect && (groupOnlyFields.length || sponsorOnlyFields.length)) {
    const syncMemberFields = () => {
      const isGroup = memberTypeSelect.value === '團體會員';
      const isSponsor = memberTypeSelect.value === '贊助會員';
      groupOnlyFields.forEach(el => { el.style.display = isGroup ? '' : 'none'; });
      sponsorOnlyFields.forEach(el => { el.style.display = isSponsor ? '' : 'none'; });
    };
    memberTypeSelect.addEventListener('change', syncMemberFields);
    syncMemberFields();
  }

  // 入會申請表單（Netlify Forms）
  const joinForm = document.querySelector('#join-form');
  if (joinForm) {
    joinForm.addEventListener('submit', (e) => {
      e.preventDefault();
      submitToNetlify(joinForm, '已收到申請，協會將盡快與您聯繫', '送出失敗，請稍後再試或改用電話聯絡', 3200);
    });
  }

  // 背景音樂：於使用者第一次互動時嘗試播放（比照芳心網站做法）
  // 瀏覽器禁止頁面完全沒有互動就自動播放有聲音的內容，因此改為
  // 「使用者第一次與頁面互動（點擊／按鍵／觸控）時自動開始播放」，
  // 體感上接近一進站就播放，同時仍符合瀏覽器政策。
  const bgmAudio = document.querySelector('#bgm-audio');
  const musicToggle = document.querySelector('#music-toggle');
  if (bgmAudio && musicToggle) {
    const STORAGE_KEY = 'tlcpea-bgm-playing';
    let autoplayAttempted = false;

    const setPlayingUI = (playing) => {
      musicToggle.classList.toggle('playing', playing);
      musicToggle.setAttribute('aria-pressed', playing ? 'true' : 'false');
    };

    const userHasPaused = () => sessionStorage.getItem(STORAGE_KEY) === '0';

    // 使用者手動按播放／暫停鍵
    musicToggle.addEventListener('click', () => {
      if (bgmAudio.paused) {
        bgmAudio.play().then(() => {
          setPlayingUI(true);
          sessionStorage.setItem(STORAGE_KEY, '1');
        }).catch(() => {});
      } else {
        bgmAudio.pause();
        setPlayingUI(false);
        sessionStorage.setItem(STORAGE_KEY, '0');
      }
    });

    // 第一次有效使用者手勢（點擊／按鍵／觸控，不含捲動）時嘗試播放
    const tryAutoplayOnFirstInteraction = () => {
      if (autoplayAttempted || userHasPaused() || !bgmAudio.paused) return;
      autoplayAttempted = true;
      bgmAudio.play().then(() => {
        setPlayingUI(true);
        sessionStorage.setItem(STORAGE_KEY, '1');
      }).catch(() => {
        autoplayAttempted = false;
      });
    };
    ['click', 'keydown', 'touchend', 'pointerdown'].forEach((evt) => {
      window.addEventListener(evt, tryAutoplayOnFirstInteraction, { once: true, passive: true });
    });

    // 若本次瀏覽（同一分頁）已經在其他頁面播放過，切頁時延續播放狀態
    if (sessionStorage.getItem(STORAGE_KEY) === '1') {
      bgmAudio.play().then(() => setPlayingUI(true)).catch(() => setPlayingUI(false));
    } else {
      setPlayingUI(false);
    }
  }
});
