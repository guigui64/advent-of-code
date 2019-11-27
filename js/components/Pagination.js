import 'bootstrap/dist/css/bootstrap.min.css';
import Link from 'next/link';

// Create days array (1 to 25)
let days = [];
for (let day = 1; day <= 25; day++) {
  days.push(day);
}

/*
 * Props are :
 *              year
 *              currentDay
 */
const Pagination = (props) => (
  <nav aria-label="Days pagination">
    <ul class="pagination justify-content-center">
      {/*<li class={'page-item' + (props.currentDay == 1 ? ' disabled' : '')}>
        <Link href={`/${props.year}-${props.currentDay - 1}`}><a class="page-link" href="#" tabindex="-1">Previous</a></Link>
      </li>*/}
      { days.map((day) => (
        <li class={'page-item' + (props.currentDay == day ? ' active' : '')}>
          <Link href={`/${props.year}-${day}`}><a class="page-link" href="#">{day}
            {props.currentDay == day &&
              <span class="sr-only">(current)</span>
            }
          </a></Link>
        </li>
      ))}
      {/*<li class={'page-item' + (props.currentDay == 25 ? ' disabled' : '')}>
        <Link href={`/${props.year}-${props.currentDay + 1}`}><a class="page-link" href="#">Next</a></Link>
      </li>*/}
    </ul>
  </nav>
);

export default Pagination;
