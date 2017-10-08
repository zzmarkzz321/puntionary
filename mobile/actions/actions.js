import { SUBMIT_INPUT } from '../constants';
import { requests } from '../util';

export function fetchPun() {
    return (dispatch) => {
        requests.fetchPun().catch((err) => {
            console.log(err);
        });
    }
}