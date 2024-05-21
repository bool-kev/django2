
const container = document.querySelector('.container');
const prev = document.getElementById('prev');
const next = document.getElementById('next'); 
const numPage = document.getElementById('numPage');

const myDoc = {
    pdf: null,
    currentPage: 1,
    scale: 2
}
pdfjsLib.getDocument(fichier).promise.then((pdf) => {
    myDoc.pdf = pdf;
    render();
});

const render = () => {
    myDoc.pdf.getPage(myDoc.currentPage).then((page) => {
        numPage.textContent = myDoc.currentPage;
        const canvas = document.getElementById('pdf_renderer');
        const ctx = canvas.getContext('2d');
        const viewport = page.getViewport({scale: myDoc.currentPage});
        canvas.height = viewport.height;
        canvas.width = viewport.width;
        page.render({
            canvasContext: ctx,
            viewport: viewport
        });
    })
}

next.addEventListener('click', () => {
    if(myDoc.pdf == null || myDoc.currentPage > myDoc.pdf._pdfInfo.numPages)
        return;
    myDoc.currentPage += 1;
    render();
});

prev.addEventListener('click', () => {
    if(myDoc.pdf == null || myDoc.currentPage == 1)
        return;
    myDoc.currentPage -= 1;
    render();
});
