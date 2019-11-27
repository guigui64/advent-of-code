import { useState } from 'react';

import DayLayout from '../components/DayLayout';
import * as aoc from '../aoc/2018-6';

const Page = (props) => {
  const [input, setInput] = useState(`165, 169
334, 217
330, 227
317, 72
304, 232
115, 225
323, 344
161, 204
316, 259
63, 250
280, 205
84, 282
271, 158
190, 296
106, 349
171, 178
203, 108
89, 271
193, 254
111, 210
341, 343
349, 311
143, 172
170, 307
128, 157
183, 315
211, 297
74, 281
119, 164
266, 345
184, 62
96, 142
134, 61
117, 52
318, 72
338, 287
61, 215
323, 255
93, 171
325, 249
183, 171
71, 235
329, 306
322, 219
151, 298
180, 255
336, 291
72, 300
223, 286
179, 257`);
  const [solutionPart1, setSolutionPart1] = useState('');
  const [solutionPart2, setSolutionPart2] = useState('');

  return (
    <DayLayout
      years={[2018, 2017, 2016, 2015]}
      year={2018}
      day={6}
      title="Chronal Coordinates"
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
