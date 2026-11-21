// Đánh dấu tính năng mới: viết [MỚI] trong markdown
const NEW_TAG = '[MỚI]';
const NEW_BADGE = '<span class="badge-new">Tính năng mới</span>';

// Gói zip chứa toàn bộ file demo (tạo bằng demo-files/_gen/sync_site_files.py)
const DEMO_ZIP_URL = 'files/copilot-workshop-demo-files.zip';

// File demo cho buổi học. url là đường dẫn trong thư mục files/ của site (tải về với tên đầy đủ),
// hoặc link ngoài (SharePoint) mở ở tab mới.
// Trong Markdown, viết [tên file](#file-<id>) để link tới file tương ứng.
const demoFiles = [
    { id: 'report', name: 'Báo cáo quản lý Q3 2026 (bản nháp).docx', desc: 'Lab 2 - Word, Lab 5 - Outlook', icon: 'word', url: 'files/bao-cao-quan-ly-q3-2026-ban-nhap.docx' },
    { id: 'handbook', name: 'Sổ tay Chính sách Nội bộ.docx', desc: 'Lab 2 - Word, Lab 8 - Agent Builder', icon: 'word', url: 'files/so-tay-chinh-sach-noi-bo.docx' },
    { id: 'policy-sample', name: 'SAMPLE Chính sách Bảo mật Thông tin.docx', desc: 'Lab 2 - Word (tự thực hành thêm)', icon: 'word', url: 'files/sample-chinh-sach-bao-mat-thong-tin.docx' },
    { id: 'business', name: 'Báo cáo Kết quả Kinh doanh Q3 2026.xlsx', desc: 'Lab 1 - Copilot Chat, Lab 3 - Excel, Lab 7 - Researcher', icon: 'excel', url: 'files/bao-cao-ket-qua-kinh-doanh-q3-2026.xlsx' },
    { id: 'feedback', name: 'Phản hồi khách hàng T9-T10 2026 (xuất từ hệ thống).xlsx', desc: 'Lab 3 - Excel (tạo skill)', icon: 'excel', url: 'files/phan-hoi-khach-hang-t9-t10-2026.xlsx' },
    { id: 'memo-template', name: 'Mẫu tờ trình (giả định).docx', desc: 'Lab 2 - Word (soạn tờ trình trên mẫu có sẵn)', icon: 'word', url: 'files/mau-to-trinh-gia-dinh.docx' },
    { id: 'plan', name: 'Kế hoạch Hoạt động 2027 (dự thảo).docx', desc: 'Lab 1 - Copilot Chat, Lab 2 - Word, Lab 4 - PowerPoint, Lab 7 - Researcher', icon: 'word', url: 'files/ke-hoach-hoat-dong-2027.docx' },
    { id: 'transcript', name: 'Transcript họp giao ban quý 3 (mẫu).docx', desc: 'Lab 6 - Teams', icon: 'word', url: 'files/transcript-hop-giao-ban-q3-mau.docx' },
    { id: 'townhall', name: 'Town hall Q3 2026 (bản nháp).pptx', desc: 'Lab 4 - PowerPoint (bộ slide có sẵn)', icon: 'powerpoint', url: 'files/town-hall-q3-2026-ban-nhap.pptx' },
    { id: 'brand', name: 'Mẫu thương hiệu (giả định).pptx', desc: 'Lab 4 - PowerPoint (mẫu thương hiệu)', icon: 'powerpoint', url: 'files/mau-thuong-hieu-gia-dinh.pptx' },
    { id: 'skill-excel', name: 'Skill Excel - bao-cao-phan-hoi-khach-hang.zip', desc: 'Lab 3 - Excel (skill mẫu)', icon: 'zip', url: 'files/skill-excel-bao-cao-phan-hoi-khach-hang.zip' },
    { id: 'skill-ppt', name: 'Skill PowerPoint - slide-tom-tat-dieu-hanh.zip', desc: 'Lab 4 - PowerPoint (skill mẫu, dự phòng)', icon: 'zip', url: 'files/skill-ppt-slide-tom-tat-dieu-hanh.zip' },
    { id: 'skill-chat', name: 'Skill Copilot Chat - bao-cao-tuan.zip', desc: 'Lab 8 - Skills in Copilot Chat (skill mẫu cho phần tự thực hành)', icon: 'zip', url: 'files/skill-chat-bao-cao-tuan.zip' },
];

// Video demo cho các bài dài. Trong Markdown, viết [video:<id>] trên một dòng riêng.
// url = '#' thì nút được ẩn (chưa có video); điền link Stream/SharePoint/YouTube khi có.
const demoVideos = {
    'word-track-changes': { title: 'Copilot sửa báo cáo bằng Track Changes', url: '#' },
    'word-memo-template': { title: 'Điền tờ trình trên mẫu có sẵn', url: '#' },
    'excel-canvas': { title: 'Dashboard tương tác với Interactive canvas', url: '#' },
    'excel-skill': { title: 'Tạo và chạy skill trong Excel', url: '#' },
    'ppt-update-deck': { title: 'Cập nhật bộ slide có sẵn theo mẫu thương hiệu', url: '#' },
    'ppt-skill': { title: 'Thêm và chạy skill trong PowerPoint', url: '#' },
};

// Danh sách module và file markdown tương ứng
const modules = {
    'module-1': { title: 'Module 1 - Giới thiệu Copilot và chuẩn bị', file: 'labs/module-1/index.md' },
    'module-2': { title: 'Module 2 - Viết prompt hiệu quả', file: 'labs/module-2/index.md' },
    'module-3': { title: 'Module 3 - Personalization in Copilot', file: 'labs/module-3/index.md' },
    'lab-1':    { title: 'Lab 1 - Copilot Chat', file: 'labs/lab-1/index.md' },
    'lab-2':    { title: 'Lab 2 - Copilot trong Word', file: 'labs/lab-2/index.md' },
    'lab-3':    { title: 'Lab 3 - Copilot trong Excel', file: 'labs/lab-3/index.md' },
    'lab-4':    { title: 'Lab 4 - Copilot trong PowerPoint', file: 'labs/lab-4/index.md' },
    'lab-5':    { title: 'Lab 5 - Copilot trong Outlook', file: 'labs/lab-5/index.md' },
    'lab-6':    { title: 'Lab 6 - Copilot trong Teams', file: 'labs/lab-6/index.md' },
    'lab-7':    { title: 'Lab 7 - Researcher Agent', file: 'labs/lab-7/index.md' },
    'lab-8':    { title: 'Lab 8 - Agent Builder: tạo agent và đưa vào Teams', file: 'labs/lab-8/index.md' },
    'wrap':     { title: 'Tổng kết', file: 'labs/wrap/index.md' }
};

// Tải và hiển thị một module
async function loadModule(key, section) {
    const mod = modules[key];
    if (!mod) return;
    const content = document.getElementById('module-content');

    try {
        const res = await fetch(mod.file, { cache: 'no-cache' });
        if (!res.ok) throw new Error(`Không tải được ${mod.file}`);
        content.innerHTML = marked.parse(await res.text());
        processCustomBlocks(content);
    } catch (err) {
        content.innerHTML = `<blockquote class="note"><p>Không tải được nội dung <code>${mod.file}</code>.
            Hãy mở trang qua một web server (ví dụ VS Code Live Server) thay vì mở trực tiếp file.</p><p>${escapeHtml(err.message)}</p></blockquote>`;
    }

    updateSidebar(key);
    showView('module');
    // Cuộn tức thì (CSS smooth scroll bị ngắt khi vừa đổi nội dung), chừa chỗ cho header cố định
    const target = section && document.getElementById(section);
    const top = target ? target.getBoundingClientRect().top + window.scrollY - 80 : 0;
    window.scrollTo({ top, behavior: 'instant' });
}

// Chuyển blockquote đặc biệt thành thẻ TIP / NOTE / PROMPT
function processCustomBlocks(content) {
    // "[MỚI]" trong tiêu đề hoặc bảng -> nhãn "Tính năng mới" (id của tiêu đề không chứa nhãn)
    content.querySelectorAll('h2, h3').forEach(h => { h.id = slugify(h.textContent.replace(NEW_TAG, '')); });
    content.querySelectorAll('h2, h3, td, li, p').forEach(el => {
        if (el.innerHTML.includes(NEW_TAG)) el.innerHTML = el.innerHTML.split(NEW_TAG).join(NEW_BADGE);
    });

    content.querySelectorAll('blockquote').forEach(bq => {
        const html = bq.innerHTML;
        if (html.includes('[!TIP]')) {
            bq.className = 'tip';
            bq.innerHTML = html.replace(/\[!TIP\]/g, '').trim();
        } else if (html.includes('[!OUTCOME]')) {
            bq.replaceWith(buildOutcomeCard(html.replace(/\[!OUTCOME\]/g, '')));
        } else if (html.includes('[!NOTE]')) {
            bq.className = 'note';
            bq.innerHTML = html.replace(/\[!NOTE\]/g, '').trim();
        } else if (html.includes('<strong>PROMPT:</strong>')) {
            const inner = html.replace(/<p><strong>PROMPT:<\/strong><\/p>/g, '').replace(/<strong>PROMPT:<\/strong>/g, '').trim();
            bq.insertAdjacentHTML('afterend', buildPromptCard(inner));
            bq.remove();
        }
    });

    // ```skill ... ``` -> khung nội dung skill (SKILL.md) có nút sao chép, giữ nguyên xuống dòng
    content.querySelectorAll('pre > code.language-skill').forEach(code => {
        const text = code.textContent.replace(/\n$/, '');
        code.parentElement.outerHTML = `<div class="prompt-card skill-card">
            <div class="prompt-card-header">
                <span class="prompt-label">Nội dung skill (SKILL.md)</span>
                <button class="copy-btn" data-copy="${escapeAttr(text)}" aria-label="Sao chép nội dung skill">
                    <span class="copy-label">Sao chép</span>
                </button>
            </div>
            <pre class="skill-body">${escapeHtml(text)}</pre>
        </div>`;
    });

    content.querySelectorAll('p').forEach(p => {
        const text = p.textContent.trim();
        if (text === '[download-files]') { p.outerHTML = buildDownloadBlock(); return; }
        const m = text.match(/^\[video:([\w-]+)\]$/);
        if (!m) return;
        const v = demoVideos[m[1]];
        if (!v || !v.url || v.url === '#') { p.remove(); return; }
        p.outerHTML = `<a class="video-demo" href="${v.url}" target="_blank" rel="noopener noreferrer">`
            + `<span class="video-play" aria-hidden="true">▶</span><span>Xem video demo: ${escapeHtml(v.title)}</span></a>`;
    });

    structureSections(content);

    // Ảnh: bọc trong <figure>, chú thích lấy từ alt
    content.querySelectorAll('img').forEach(img => {
        const figure = document.createElement('figure');
        figure.className = 'content-figure';
        img.classList.add('content-img');
        // marked bọc ảnh trong <p>; thay cả <p> nếu nó chỉ chứa ảnh
        const parent = img.parentElement;
        (parent.tagName === 'P' && parent.childNodes.length === 1 ? parent : img).replaceWith(figure);
        figure.appendChild(img);
        if (img.alt) {
            const caption = document.createElement('figcaption');
            caption.textContent = img.alt;
            figure.appendChild(caption);
        }
    });

    // [tên file](#file-<id>) -> link SharePoint của file đó
    content.querySelectorAll('a[href^="#file-"]').forEach(a => {
        const file = demoFiles.find(f => `#file-${f.id}` === a.getAttribute('href'));
        if (!file) return;
        // File chưa có link SharePoint: giữ nguyên chữ, bỏ liên kết
        if (file.url === '#') {
            a.removeAttribute('href');
            a.title = 'File demo đang được cập nhật';
            return;
        }
        a.href = file.url;
        if (isLocalFile(file)) {
            a.setAttribute('download', file.name);
        } else {
            a.target = '_blank';
            a.rel = 'noopener noreferrer';
        }
        a.classList.add('file-link');
    });
}

// Sắp xếp trang cho dễ đọc:
// - "Kết quả mong đợi" -> khối gập (bấm để xem), tránh lộ đáp án và giảm độ dài trang
// - mỗi bài tập (### dưới "Thực hành trong buổi học" hoặc "Phần X") -> một thẻ riêng
// - mỗi mục dưới "Tự thực hành thêm", "Prompt đề xuất" -> khối gập, chỉ hiện tiêu đề
function structureSections(content) {
    const STOP = 'h1, h2, h3, hr, ol, blockquote, .prompt-card, details, .outcome-card, .video-demo';
    // Đoạn chỉ gồm một nhãn in đậm kết thúc bằng ":" (ví dụ "Duyệt thay đổi:") mở một nhóm bước mới
    const isLabel = el => el.tagName === 'P' && el.firstElementChild && el.firstElementChild.tagName === 'STRONG'
        && el.textContent.trim() === el.firstElementChild.textContent.trim() && /:$/.test(el.textContent.trim());
    Array.from(content.children).forEach(p => {
        const label = p.firstElementChild;
        if (p.tagName !== 'P' || !label || label.tagName !== 'STRONG' || p.firstChild !== label
            || !/^Kết quả mong đợi/.test(label.textContent)) return;
        const det = document.createElement('details');
        det.className = 'answer';
        det.innerHTML = '<summary>Xem kết quả mong đợi</summary>';
        const body = document.createElement('div');
        body.className = 'answer-body';
        p.before(det);
        label.remove();
        p.innerHTML = p.innerHTML.trim();
        let next = p.nextElementSibling;
        if (p.textContent.trim()) body.appendChild(p); else p.remove();
        while (next && !next.matches(STOP) && !isLabel(next)) {
            const after = next.nextElementSibling;
            body.appendChild(next);
            next = after;
        }
        det.appendChild(body);
    });

    let mode = null;
    const groups = [];
    Array.from(content.children).forEach(el => {
        if (el.tagName === 'H2') {
            const t = el.textContent.trim();
            mode = /^(Thực hành trong buổi học|Phần [A-Z]\b)/.test(t) ? 'card'
                : /^(Tự thực hành|Prompt đề xuất)/.test(t) ? 'fold' : null;
        } else if (el.tagName === 'H3' && mode) {
            groups.push([el, mode]);
        }
    });
    groups.forEach(([h3, kind]) => {
        const wrap = document.createElement(kind === 'card' ? 'div' : 'details');
        wrap.className = kind === 'card' ? 'exercise-card' : 'extra';
        h3.before(wrap);
        let next = h3.nextElementSibling;
        if (kind === 'card') {
            wrap.appendChild(h3);
        } else {
            const summary = document.createElement('summary');
            summary.appendChild(h3);
            wrap.appendChild(summary);
        }
        while (next && !next.matches('h1, h2, h3, hr')) {
            const after = next.nextElementSibling;
            wrap.appendChild(next);
            next = after;
        }
    });
}

// Khung "Sau lab này": mỗi đoạn in đậm (Làm được / Biết được) cùng danh sách ngay sau nó thành một cột
function buildOutcomeCard(innerHtml) {
    const tmp = document.createElement('div');
    tmp.innerHTML = innerHtml;
    const card = document.createElement('div');
    card.className = 'outcome-card';
    let col = null;
    Array.from(tmp.children).forEach(el => {
        if (el.tagName === 'P' && el.querySelector('strong')) {
            col = document.createElement('div');
            col.className = 'outcome-col';
            const head = document.createElement('div');
            head.className = 'outcome-head';
            head.textContent = el.textContent.trim();
            col.appendChild(head);
            card.appendChild(col);
        } else if (col) {
            col.appendChild(el);
        }
    });
    return card;
}

// Thẻ prompt có nút sao chép
function buildPromptCard(innerHtml) {
    const tmp = document.createElement('div');
    tmp.innerHTML = innerHtml;
    // textContent bỏ mất số thứ tự của <ol>, nên thêm lại
    tmp.querySelectorAll('ol').forEach(ol => {
        Array.from(ol.children).forEach((li, i) => li.prepend(`${ol.start + i}. `));
    });
    const plainText = tmp.textContent.trim();

    return `<div class="prompt-card">
        <div class="prompt-card-header">
            <span class="prompt-label">Prompt</span>
            <button class="copy-btn" data-copy="${escapeAttr(plainText)}" aria-label="Sao chép prompt">
                <span class="copy-label">Sao chép</span>
            </button>
        </div>
        <div class="prompt-body">${innerHtml}</div>
    </div>`;
}

// Khối tải file demo
function buildDownloadBlock() {
    const colors = { excel: '#107c10', word: '#2b579a', powerpoint: '#c43e1c', pdf: '#b30b00', image: '#5c2d91', zip: '#55606e' };
    const letters = { excel: 'X', word: 'W', powerpoint: 'P', pdf: 'PDF', image: 'IMG', zip: 'ZIP' };
    const items = demoFiles.map(f => {
        const placeholder = f.url === '#';
        const linkAttrs = placeholder ? ''
            : isLocalFile(f) ? `download="${escapeAttr(f.name)}"` : 'target="_blank" rel="noopener noreferrer"';
        return `<a href="${escapeAttr(f.url)}" class="download-item${placeholder ? ' download-item--placeholder' : ''}" ${linkAttrs}>
            <span class="download-icon" style="background:${colors[f.icon]};color:#fff;font-weight:700;font-size:${letters[f.icon].length > 1 ? 11 : 16}px">${letters[f.icon]}</span>
            <span class="download-info">
                <span class="download-name">${escapeHtml(f.name)}</span>
                <span class="download-desc">${escapeHtml(f.desc)}</span>
            </span>
        </a>`;
    }).join('');

    return `<div class="download-block">
        <div class="download-block-header">
            <span>File demo cho buổi học</span>
            <a class="folder-btn" href="${escapeAttr(DEMO_ZIP_URL)}" download="File demo Copilot Workshop.zip">⬇ Tải tất cả (.zip)</a>
        </div>
        <p class="download-block-hint">Bấm vào từng file để tải về, sau đó tải lên <strong>OneDrive</strong> của anh/chị trước khi bắt đầu Lab. Xem <a href="#module-1/cach-tai-file-word-excel-ve-may">cách tải file về và đưa lên OneDrive</a>.</p>
        <div class="download-list">${items}</div>
    </div>`;
}


// Sao chép prompt (dùng event delegation)
document.addEventListener('click', async e => {
    const btn = e.target.closest('.copy-btn');
    if (!btn) return;
    const text = btn.dataset.copy;
    try {
        await navigator.clipboard.writeText(text);
    } catch {
        const ta = document.createElement('textarea');
        ta.value = text;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        ta.remove();
    }
    btn.classList.add('copied');
    btn.querySelector('.copy-label').textContent = 'Đã sao chép!';
    setTimeout(() => {
        btn.classList.remove('copied');
        btn.querySelector('.copy-label').textContent = 'Sao chép';
    }, 2000);
});

// File nằm trong site (không phải link ngoài như SharePoint)
function isLocalFile(file) {
    return !/^https?:/i.test(file.url);
}

function escapeHtml(str) {
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function escapeAttr(str) {
    return str.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/\n/g, '&#10;');
}

function updateSidebar(activeKey) {
    document.getElementById('module-nav').innerHTML = Object.entries(modules)
        .map(([key, mod]) => `<a href="#${key}" class="${key === activeKey ? 'active' : ''}">${mod.title}</a>`)
        .join('');
}

function showView(name) {
    document.getElementById('home-view').classList.toggle('active', name === 'home');
    document.getElementById('module-view').classList.toggle('active', name === 'module');
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.toggle('active', name === 'home' && link.dataset.view === 'home');
    });
}

// Điều hướng bằng hash: #lab-1 mở lab, #module-1/<section> mở lab và cuộn tới mục đó
function route() {
    const [key, section] = location.hash.replace('#', '').split('/');
    if (modules[key]) loadModule(key, section);
    else showView('home');
}

// "Cách tải file Word/Excel về máy" -> "cach-tai-file-word-excel-ve-may"
function slugify(text) {
    return text.normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/đ/g, 'd').replace(/Đ/g, 'D')
        .toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', e => {
        e.preventDefault();
        history.pushState(null, '', location.pathname);
        showView('home');
        if (link.dataset.view === 'agenda') document.querySelector('.agenda-section').scrollIntoView();
        else window.scrollTo(0, 0);
    });
});

window.addEventListener('hashchange', route);
route();
