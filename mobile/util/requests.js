import axios from 'axios';

const BASE_URI = 'http://localhost:3000'

export const request = {
    fetchPun() {
        axios.post(BASE_URI + '/test', {
            'key': 'Testing string! Replace me with something Dynamic'
        })
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        });
    }
}
