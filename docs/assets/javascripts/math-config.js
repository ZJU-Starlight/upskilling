window.MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)']],
    displayMath: [['\\[', '\\]']],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: '.*|',
    processHtmlClass: 'arithmatex'
  },
  svg: { fontCache: 'global' },
  startup: {
    ready() {
      MathJax.startup.defaultReady();
      if (typeof document$ !== 'undefined') {
        document$.subscribe(() => {
          MathJax.startup.promise.then(() => MathJax.typesetPromise());
        });
      }
    }
  }
};
