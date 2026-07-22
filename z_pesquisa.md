        <form id="form-contato" method="GET" action="processamento.htm" onsubmit="return revisarEnvio(event)">

            <!-- DADOS PESSOAIS -->
            <fieldset>
                <legend>Dados pessoais</legend>

                <div class="campo">
                    <label for="nome">Nome completo</label>
                    <input type="text" id="nome" name="nome" placeholder="Digite seu nome completo" minlength="3" required>
                </div>

                <div class="campo">
                    <label for="email">E-mail</label>
                    <input type="email" id="email" name="email" placeholder="seuemail@exemplo.com" required>
                </div>

                <div class="campo">
                    <label for="telefone">Telefone</label>
                    <input type="tel" id="telefone" name="telefone"
                           placeholder="(00) 00000-0000"
                           pattern="\(\d{2}\)\s?\d{4,5}-\d{4}"
                           title="Formato esperado: (00) 00000-0000"
                           required>
                </div>
            </fieldset>


            <!-- DETALHES DA MENSAGEM -->
            <fieldset>
                <legend>Detalhes da mensagem</legend>

                <div class="campo">
                    <label for="assunto">Assunto</label>
                    <select id="assunto" name="assunto" required>
                        <option value="" disabled selected hidden>Selecione uma opção</option>
                        <option value="Duvida">Dúvida</option>
                        <option value="Sugestao">Sugestão</option>
                        <option value="Critica">Crítica</option>
                    </select>
                </div>

                <div class="campo campo-radio">
                    <span class="rotulo-grupo">Perfil do usuário</span>

                    <div class="opcao-radio">
                        <input type="radio" id="perfil-aluno" name="perfil" value="Aluno" required>
                        <label for="perfil-aluno">Aluno</label>
                    </div>

                    <div class="opcao-radio">
                        <input type="radio" id="perfil-professor" name="perfil" value="Professor" required>
                        <label for="perfil-professor">Professor</label>
                    </div>

                    <div class="opcao-radio">
                        <input type="radio" id="perfil-comunidade" name="perfil" value="Comunidade Externa" required>
                        <label for="perfil-comunidade">Comunidade Externa</label>
                    </div>
                </div>

                <div class="campo">
                    <label for="mensagem">Mensagem</label>
                    <textarea id="mensagem" name="mensagem" rows="5" minlength="15"
                              placeholder="Escreva sua mensagem (mínimo de 15 caracteres)" required></textarea>
                </div>
            </fieldset>

            <button type="submit" id="botao-enviar">Enviar</button>

        </form>









            // função do formulário de Contato (contato.htm) ➡ fica aqui porque scripts dentro
            // de um fragmento carregado via innerHTML não são executados pelo navegador
            function revisarEnvio(evento) {
                evento.preventDefault();     // impede o envio automático inicial

                const form = evento.target;

                // garante que a validação nativa (required, pattern, minlength...) já passou
                if (!form.checkValidity()) {
                    form.reportValidity();   // mostra a mensagem nativa do navegador
                    return false;
                }

                const nome = form.nome.value;
                const email = form.email.value;
                const telefone = form.telefone.value;
                const assunto = form.assunto.options[form.assunto.selectedIndex].text;
                const perfilSelecionado = form.querySelector('input[name="perfil"]:checked');
                const perfil = perfilSelecionado ? perfilSelecionado.value : '';
                const mensagem = form.mensagem.value;

                const resumo =
                    "Revise os dados antes de enviar:\n\n" +
                    "Nome: " + nome + "\n" +
                    "E-mail: " + email + "\n" +
                    "Telefone: " + telefone + "\n" +
                    "Assunto: " + assunto + "\n" +
                    "Perfil: " + perfil + "\n" +
                    "Mensagem: " + mensagem;

                if (confirm(resumo)) {
                    form.submit();     // Confirmar --> envio real via GET
                }
                // Cancelar --> não faz nada, o formulário permanece preenchido para correção

                return false;





<script>

    // captura os parâmetros anexados na URL pelo envio do formulário (method="GET")
    const parametros = new URLSearchParams(window.location.search);

    const nome = parametros.get('nome');
    const email = parametros.get('email');

    // mensagem de sucesso personalizada com nome e e-mail capturados da URL
    document.getElementById('destaque-nome').textContent = nome || 'visitante';
    document.getElementById('destaque-email').textContent = email || 'não informado';

    // dados complementares, também capturados via URLSearchParams
    document.getElementById('resumo-telefone').textContent = parametros.get('telefone') || '-';
    document.getElementById('resumo-assunto').textContent = parametros.get('assunto') || '-';
    document.getElementById('resumo-perfil').textContent = parametros.get('perfil') || '-';
    document.getElementById('resumo-mensagem').textContent = parametros.get('mensagem') || '-';

    // caso a página seja aberta sem nenhum parâmetro (acesso direto), avisa o usuário
    if (!nome && !email) {
        document.getElementById('titulo-sucesso').textContent = 'Nenhum dado recebido';
        document.getElementById('mensagem-personalizada').textContent =
            'Esta página exibe a confirmação depois do envio do formulário de Contato. Volte e preencha o formulário primeiro.';
        document.getElementById('tabela-resumo-envio').style.display = 'none';
    }

</script>