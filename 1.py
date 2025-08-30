
import React, { useState } from 'react';

const choices = ['rock', 'paper', 'scissors'];

const RockPaperScissors = () => {
  const [userChoice, setUserChoice] = useState('');
  const [computerChoice, setComputerChoice] = useState('');
  const [result, setResult] = useState('');

  const handleUserChoice = (choice: string) => {
    setUserChoice(choice);
    const randomIndex = Math.floor(Math.random() * choices.length);
    setComputerChoice(choices[randomIndex]);
    determineWinner(choice, choices[randomIndex]);
  };

  const determineWinner = (user: string, computer: string) => {
    if (user === computer) {
      setResult('It\'s a tie!');
    } else if ((user === 'rock' && computer === 'scissors') || (user === 'scissors' && computer === 'paper') || (user === 'paper' && computer === 'rock')) {
      setResult('You win!');
    } else {
      setResult('You lose!');
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-3xl font-bold mb-4">Rock, Paper, Scissors</h1>
      <div className="flex justify-around w-full">
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onClick={() => handleUserChoice('rock')}>Rock</button>
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onClick={() => handleUserChoice('paper')}>Paper</button>
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onClick={() => handleUserChoice('scissors')}>Scissors</button>
      </div>
      <p className="text-2xl font-bold mt-4">You chose: {userChoice}</p>
      <p className="text-2xl font-bold mt-4">Computer chose: {computerChoice}</p>
      <p className="text-2xl font-bold mt-4">{result}</p>
    </div>
  );
};

export default RockPaperScissors;