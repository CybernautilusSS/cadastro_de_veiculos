    const campoImagem = document.getElementById('{{ form.imagem.id_for_label }}');
    const preview = document.getElementById('imagem-preview');

    campoImagem.addEventListener('change', function () {

        const arquivo = this.files[0];

        if (arquivo) {

            preview.src = URL.createObjectURL(arquivo);
            preview.style.display = 'block';

        } else {

            preview.src = '';
            preview.style.display = 'none';

        }

    });