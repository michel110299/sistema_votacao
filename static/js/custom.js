function validaDatas(){
    var dataInicial = new Date($("input[name='horario_inicio']").val());
    var dataFinal = new Date($("input[name='horario_termino']").val());
    if (!dataInicial || !dataFinal) return false;
    if (dataInicial >= dataFinal) {
        var toastHTML = '<span>Data Invalida!</span><button class="btn-flat toast-action">ok</button>';
        M.toast({html: toastHTML});
        return false;
    } else {
        return true
    }
}