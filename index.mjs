import clipboard from 'clipboardy';

const enterprises = ["Agrisan", "LFG", "Agrovence", "Panarello", "PrimeFoods", "Santa Rita"];

let gabrielScale = [];
let eduardoScale = [];

const determineScale = (gabrielScale, eduardoScale) => {

    for(let index in enterprises){

        let addEntreprise = enterprises[Math.floor(Math.random()*6)]

        while(gabrielScale.includes(addEntreprise) || eduardoScale.includes(addEntreprise)){
            addEntreprise = enterprises[Math.floor(Math.random()*6)];
        }

        if(!gabrielScale.includes(addEntreprise) && gabrielScale.length < 3)
            gabrielScale.push(addEntreprise);
        else if(!eduardoScale.includes(addEntreprise))
            eduardoScale.push(addEntreprise);
    }

}

const scaleDayGenerator = () => {
    const date = new Date();

    const day = date.getDate() < 10 ? `0${date.getDate()}` : `${date.getDate()}`;
    const month = date.getMonth() + 1 < 10 ? `0${date.getMonth() + 1}` : `${date.getMonth() + 1}`;

    return `${day}/${month}/${date.getFullYear()}`;
}

determineScale(gabrielScale, eduardoScale);

clipboard.write(`*📄 Escala de Atendimento de Suporte ${scaleDayGenerator()}*

Segue abaixo a escala de atendimentos para o dia presente:
        
⚫⚪ Gabriel M. V. Braga:
        
- ${gabrielScale[0]}
- ${gabrielScale[1]}
- ${gabrielScale[2]}
        
🔵⚪ Eduardo J. Borges:
        
- ${eduardoScale[0]}
- ${eduardoScale[1]}
- ${eduardoScale[2]}
`);
