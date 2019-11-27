import { useState } from 'react';

import DayLayout from '../components/DayLayout';
import * as aoc from '../aoc/2018-9';

const Page = (props) => {
  const [input, setInput] = useState(`459 players; last marble is worth 71790 points`);
  const [solutionPart1, setSolutionPart1] = useState('');
  const [solutionPart2, setSolutionPart2] = useState('');

  return (
    <DayLayout
      years={[2018, 2017, 2016, 2015]}
      year={2018}
      day={9}
      title="Marble Mania"
      input={input}
      handleInputChange={e => {
        setInput(e.target.value);
        setSolutionPart1('');
        setSolutionPart2('');
      }}
      solveAll={() => {
        const [part1, part2] = aoc.all(input);
        setSolutionPart1(part1);
        setSolutionPart2(part2);
      }}
      solutionPart1={solutionPart1}
      solutionPart2={solutionPart2}
    />
  );
}

export default Page;
