// https://www.codewars.com/kata/57ecf6efc7fe13eb070000e1/

// Passed

function outed(meet, boss){
    let totalScore = Object.values(meet).reduce((previous, current) => previous + current, 0);
    totalScore += meet[boss];

    const happinnessRating = totalScore / Object.keys(meet).length;

    return happinnessRating <=5 ? 'Get Out Now!' : 'Nice Work Champ!';
}

const output = outed({'tim':0, 'jim':2, 'randy':0, 'sandy':7, 'andy':0, 'katie':5, 'laura':1, 'saajid':2, 'alex':3, 'john':2, 'mr':0}, 'laura');
console.log(output); 