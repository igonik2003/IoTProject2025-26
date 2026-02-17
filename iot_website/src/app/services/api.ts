import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class Api {

  private baseUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  testConnection() {
    return this.http.get(this.baseUrl);
  }

  getSensorData(piId: string, sensorId: string) {
  return this.http.get(
    `http://127.0.0.1:8000/sensor/${piId}/${sensorId}`
  );
}
}
