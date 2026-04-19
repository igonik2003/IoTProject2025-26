import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { Api } from '../services/api';
import { FormsModule } from '@angular/forms';
@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule,FormsModule],
  templateUrl: './home.html',
  styleUrls: ['./home.css']
})
export class Home{

  constructor(private router: Router,private api: Api) {}
  timerSeconds: number = 0;
  addSeconds: number = 0;

  webPin: string = '';

  alarmStatus: any;
  peopleCount: any;

  dht1Temp: any;
  dht1Hum: any;

  dht2Temp: any;
  dht2Hum: any;

  dht3Temp: any;
  dht3Hum: any;
  pi1Cards = [
    {id:'ds1', title: 'DS1 DOOR BUTTON SENSOR', image: 'https://i.ebayimg.com/images/g/VP0AAOSwq4NanhVL/s-l1200.jpg' },
    {id:'dpir1', title: 'DPIR1 MOTION SENSOR', image: 'https://res.cloudinary.com/rsc/image/upload/b_rgb:FFFFFF,c_pad,dpr_2.625,f_auto,h_214,q_auto,w_380/c_pad,h_214,w_380/F7813024-01?pgw=1' },
    {id:'dus1', title: 'DUS1 DISTANCE SENSOR', image: 'https://cdn-wordpress-info.futurelearn.com/info/wp-content/uploads/8-Distance_sensor-768x514.png' },
    {id:'db', title: "DB DOOR BUZZER", image: "https://www.electronicaembajadores.com/Datos/fotos/articulos/grandes/zb/zbmg/zbmg006.jpg"},
    {id:'dl', title: "DL DOOR LIGHT", image: "https://dxv0kh7euhy9z.cloudfront.net/catalog/product/cache/67cb7de173f5275efcd98ea89f80cd4b/3/1/31mm_hp6_cool_pair_door_titled.jpg"},
    {id:'dms', title: "DMS DOOR MEMBRANE SWITCH", image: "data:image/jpeg;base64,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"}
  ];

  pi2Cards = [
    {id:'ds2', title: 'DS2 DOOR BUTTON SENSOR', image: 'https://i.ebayimg.com/images/g/VP0AAOSwq4NanhVL/s-l1200.jpg' },
    {id:'dpir2', title: 'DPIR2 MOTION SENSOR', image: 'https://res.cloudinary.com/rsc/image/upload/b_rgb:FFFFFF,c_pad,dpr_2.625,f_auto,h_214,q_auto,w_380/c_pad,h_214,w_380/F7813024-01?pgw=1' },
    {id:'dus2', title: 'DUS2 DISTANCE SENSOR', image: 'https://cdn-wordpress-info.futurelearn.com/info/wp-content/uploads/8-Distance_sensor-768x514.png' },
    {id:'btn', title: 'BTN KITCHEN BUTTON', image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZvRFo6mhNFXdHCAeE-_w5k3kACXM7yKZh9g&s' },
    {id:'4sd', title: '4SD DISPLAY', image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQX7Efpv25bnjIQDQSKVl9Z_BH0S7sr8tr8kA&s' },
    {id:'dht3', title: 'DHT3 Kitchen DHT', image: 'https://www.kiwi-electronics.com/image/cache/catalog/product/5xp3271y/C-DHT11_0-800x533.jpg' },
    {id:'gsg', title: 'GSG Gyroscope', image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0oDQnUkrO9MoxywX2LW3xboCMGn4FJfasCA&s' }
  ];

  pi3Cards = [
    {id:'dpir3', title: 'DPIR3 LIVING ROOM MOTION SENSOR', image: 'https://res.cloudinary.com/rsc/image/upload/b_rgb:FFFFFF,c_pad,dpr_2.625,f_auto,h_214,q_auto,w_380/c_pad,h_214,w_380/F7813024-01?pgw=1' },
    {id:'dht1', title: 'DHT1 BEDROOM DHT', image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdgbqWnlgsO3ZShlWpfRE4hY3EcsheZl3aWw&s'}, 
    {id:'dht2', title: 'DHT2 MASTER BEDROOM DHT', image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdYv6CoLYuiNOio4BTYAL9t0ikK9LE6kHfAw&s'},
    {id:'ir', title: 'IR BEDROOM INFRARED', image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSpsOnigAug_fBoPQY6oq_pw5JjP4aFxhbrQ&s'},
    {id:'brgb', title: 'BRGB BEDROOM RGB', image: 'https://www.safelinemart.com/images/products/led-night-lights-bedside-table-lamp-with-rgb-color-changing-mode-warm-white-dimmable-light-rechargeable-led-kids-baby-night-lamp-for-bedroom-with-type-c-charging-cable60bbe9119f795380284bac0b338d501230d8d140.jpg'},
    {id:'lcd', title: 'LCD LIVING ROOM DISPLAY', image: 'https://hobbycomponents.com/2469-large_default/hobby-components-1602-smart-lcd.jpg'}
  ];

  alarm=[
    {id:'alarm', title: 'ALARM', image: 'https://static.vecteezy.com/system/resources/thumbnails/023/209/812/small/alarm-icon-on-white-background-alarm-sign-flat-style-vector.jpg'}
  ]

  goToDetails(piId: string, sensorId: string) {
  this.router.navigate(['/details', piId, sensorId]);
  }
  saveTimerSettings() {
    this.api.setTimerSettings(this.timerSeconds)
      .subscribe({
        next: () => console.log("Timer settings sent"),
        error: (err) => console.error(err)
      });
  }

  saveTimerSettings1() {
    this.api.setTimerSettings1(this.addSeconds)
      .subscribe({
        next: () => console.log("Timer1 settings sent"),
        error: (err) => console.error(err)
      });
  }

  sendPin() {
    this.api.verifyPin(this.webPin).subscribe({
      next: (res: any) => {
        console.log(res.status);
        this.webPin = '';
      },
      error: (err) => console.error(err)
    });
  }

  setRGB(r: number, g: number, b: number) {
    this.api.setRGB(r, g, b).subscribe({
      next: () => console.log("RGB updated"),
      error: (err) => console.error(err)
    });
  }


  ngOnInit() {

    this.api.testConnection().subscribe({
      next: (res) => console.log("Backend response:", res),
      error: (err) => console.error("Connection error:", err)
    });

  }
}
