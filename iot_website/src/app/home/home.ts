import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { Api } from '../services/api';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './home.html',
  styleUrls: ['./home.css']
})
export class Home{

  constructor(private router: Router,private api: Api) {}

  pi1Cards = [
    {id:'ds1', title: 'DS1 DOOR BUTTON SENSOR', image: 'https://i.ebayimg.com/images/g/VP0AAOSwq4NanhVL/s-l1200.jpg' },
    {id:'dpir1', title: 'DPIR1 MOTION SENSOR', image: 'https://res.cloudinary.com/rsc/image/upload/b_rgb:FFFFFF,c_pad,dpr_2.625,f_auto,h_214,q_auto,w_380/c_pad,h_214,w_380/F7813024-01?pgw=1' },
    {id:'dus1', title: 'DUS1 DISTANCE SENSOR', image: 'https://cdn-wordpress-info.futurelearn.com/info/wp-content/uploads/8-Distance_sensor-768x514.png' }
  ];

  pi2Cards = [
    {id:'ds2', title: 'DS2 DOOR BUTTON SENSOR', image: 'https://i.ebayimg.com/images/g/VP0AAOSwq4NanhVL/s-l1200.jpg' },
    {id:'dpir2', title: 'DPIR2 MOTION SENSOR', image: 'https://res.cloudinary.com/rsc/image/upload/b_rgb:FFFFFF,c_pad,dpr_2.625,f_auto,h_214,q_auto,w_380/c_pad,h_214,w_380/F7813024-01?pgw=1' },
    {id:'dus2', title: 'DUS2 DISTANCE SENSOR', image: 'https://cdn-wordpress-info.futurelearn.com/info/wp-content/uploads/8-Distance_sensor-768x514.png' },
    {id:'btn', title: 'BTN KITCHEN BUTTON', image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZvRFo6mhNFXdHCAeE-_w5k3kACXM7yKZh9g&s' },
    {id:'4sd', title: '4SD DISPLAY', image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQX7Efpv25bnjIQDQSKVl9Z_BH0S7sr8tr8kA&s' }
  ];

  pi3Cards = [
    {id:'dpir3', title: 'DPIR3 LIVING ROOM MOTION SENSOR', image: 'https://res.cloudinary.com/rsc/image/upload/b_rgb:FFFFFF,c_pad,dpr_2.625,f_auto,h_214,q_auto,w_380/c_pad,h_214,w_380/F7813024-01?pgw=1' },
  ];

  alarm=[
    {id:'alarm', title: 'ALARM', image: 'https://static.vecteezy.com/system/resources/thumbnails/023/209/812/small/alarm-icon-on-white-background-alarm-sign-flat-style-vector.jpg'}
  ]

  goToDetails(piId: string, sensorId: string) {
  this.router.navigate(['/details', piId, sensorId]);
  }

  ngOnInit() {
  this.api.testConnection().subscribe({
    next: (res) => console.log("Backend response:", res),
    error: (err) => console.error("Connection error:", err)
  });
}
}
