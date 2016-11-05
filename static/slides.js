Reveal.initialize({
    controls: true,
    mouseWheel: true,

    progress: true,
    history: true,
    center: true,
    transition: 'slide',
    dependencies: [
        {
            src: '../static/revealjs/lib/js/classList.js',
            condition: function () {
                return !document.body.classList;
            }
        },
        {
            src: '../static/revealjs/plugin/highlight/highlight.js',
            async: true,
            condition: function () {
                return !!document.querySelector('pre code');
            },
            callback: function () {
                hljs.initHighlightingOnLoad();
            }
        },
        {src: '../static/revealjs/plugin/notes/notes.js', async: true}
    ]
});
