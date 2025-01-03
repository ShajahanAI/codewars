// https://www.codewars.com/kata/564e21ba7cd824845b000097

// Passed

function knightVsBishop(knightPosition, bishopPosition) {
    // Three possible outputs are "Knight", "Bishop", and "None";
    
    currentBishopSquare = `${bishopPosition[1]}${bishopPosition[0]}`
    currentKnightSquare = `${knightPosition[1]}${knightPosition[0]}`

    let knightMoves = getKnightMoves(knightPosition[1], knightPosition[0]);
    let bishopMoves = getBishopMoves(bishopPosition[1], bishopPosition[0]);

    if (knightMoves.includes(currentBishopSquare)){
        return 'Knight'
    }
    else if (bishopMoves.includes(currentKnightSquare)){
        return 'Bishop'
    }

    return 'None'

}

function getKnightMoves(knightFile, knightRank){
    let files = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
    let ranks = [1, 2, 3, 4, 5, 6, 7 ,8];
    let possibleMoves = [];
    let fileIndex = files.indexOf(knightFile);
    let incrementRank = knightRank;
    let decrementRank = knightRank;

    // To the right side
    for (possibleRank = knightRank + 1; possibleRank <= knightRank + 2; possibleRank++){
        increase_decrease_value = (possibleRank - knightRank) === 1 ? 2 : -1
        incrementRank += increase_decrease_value;
        decrementRank -= increase_decrease_value;
        fileIndex++;
        if (files[fileIndex] !== undefined){
            // It's a valid file that exists on the chessboard
            let possibleFile = files[fileIndex];
            if (ranks.includes(incrementRank)){
                possibleMoves.push(`${possibleFile}${incrementRank}`);
            }

            if (ranks.includes(decrementRank)){
                possibleMoves.push(`${possibleFile}${decrementRank}`);
            }
        }
    }

    incrementRank = knightRank;
    decrementRank = knightRank;
    fileIndex = files.indexOf(knightFile);
    // To the left side
    for (possibleRank = knightRank - 1; possibleRank >= knightRank - 2; possibleRank--){
        increase_decrease_value = (knightRank - possibleRank) === 1 ? 2 : -1
        incrementRank += increase_decrease_value;
        decrementRank -= increase_decrease_value;
        fileIndex--;
        if (files[fileIndex] !== undefined){
            // It's a valid file that exists on the chessboard
            let possibleFile = files[fileIndex];
            if (ranks.includes(incrementRank)){
                possibleMoves.push(`${possibleFile}${incrementRank}`);
            }

            if (ranks.includes(decrementRank)){
                possibleMoves.push(`${possibleFile}${decrementRank}`);
            }
        }
    }
    return possibleMoves;
};


function getBishopMoves(bishopFile, bishopRank){
    let files = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
    let ranks = [1, 2, 3, 4, 5, 6, 7 ,8];
    let possibleMoves = [];
    let fileIndex = files.indexOf(bishopFile);
    let incrementRank = bishopRank;
    let decrementRank = bishopRank;

    // To the right side
    for (possibleRank = bishopRank; possibleRank < 9 | fileIndex < files.length; possibleRank++){
        incrementRank++;
        decrementRank--;
        fileIndex++;
        if (files[fileIndex] !== undefined){
            // It's a valid file that exists on the chessboard
            let possibleFile = files[fileIndex];
            if (ranks.includes(incrementRank)){
                possibleMoves.push(`${possibleFile}${incrementRank}`);
            }

            if (ranks.includes(decrementRank)){
                possibleMoves.push(`${possibleFile}${decrementRank}`);
            }
        }
    }

    // To the left side
    fileIndex = files.indexOf(bishopFile);
    incrementRank = bishopRank;
    decrementRank = bishopRank;
    for (possibleRank = bishopRank; possibleRank > 0  | fileIndex >= 0; possibleRank--){
        incrementRank++;
        decrementRank--;
        fileIndex--;
        if (files[fileIndex] !== undefined){
            // It's a valid file that exists on the chessboard
            let possibleFile = files[fileIndex];
            if (ranks.includes(incrementRank)){
                possibleMoves.push(`${possibleFile}${incrementRank}`);
            }

            if (ranks.includes(decrementRank)){
                possibleMoves.push(`${possibleFile}${decrementRank}`);
            }
        }


    }
    return possibleMoves;
}

let Moves = getKnightMoves('A', 1);

let output = knightVsBishop([5, 'E'], [4, 'D']);
console.log(output);