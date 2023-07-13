
const fdk=require('@fnproject/fdk');
const Sequelize = require('sequelize');

fdk.handle(async function(input){

    try {

        const sequelize = new Sequelize('exam4', 'admin', '.1adminSQL1.', { host: '20.1.2.234', dialect: 'mysql'});

        const lista = await sequelize.query("SELECT * FROM tipo_comida");

        return {lista}

    } catch (error) {
        console.log(error)
        return {'message': 'Something went wrong'}
    }


})







