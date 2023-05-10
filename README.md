# API-Insumo

Este é um repositório que contém uma API de consulta a informações de insumos. A API foi desenvolvida utilizando os frameworks Flask e FastAPI em Python.

## Instalação

Para instalar as dependências necessárias, execute o seguinte comando:

```
pip install -r requirements.txt
```

Para utilizar o FastAPI, é necessário instalar o Uvicorn:

```
pip install uvicorn
```

## Utilização

### Utilizando Flask

Para iniciar o servidor com Flask, execute o seguinte comando:

```
python app_flask.py
```

A API estará disponível na porta 5000. Para fazer uma consulta, envie uma requisição GET para a URL `http://localhost:5000/insumo/:id`, onde `:id` é o ID do insumo que se deseja consultar.

### Utilizando FastAPI

Para iniciar o servidor com FastAPI, execute o seguinte comando:

```
uvicorn app_fastapi:app --reload
```

A API estará disponível na porta 8000. Para fazer uma consulta, envie uma requisição GET para a URL `http://localhost:8000/insumo/:id`, onde `:id` é o ID do insumo que se deseja consultar.

## Contribuição

Contribuições são bem-vindas! Se você quiser contribuir com este projeto, siga as instruções abaixo:

1. Faça um fork deste repositório
2. Crie uma branch com sua feature: `git checkout -b minha-feature`
3. Faça o commit das suas alterações: `git commit -m 'Minha nova feature'`
4. Faça o push para a branch: `git push origin minha-feature`
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.