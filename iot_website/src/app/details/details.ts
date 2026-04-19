import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';
import { Api } from '../services/api';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-details',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './details.html',
  styleUrls: ['./details.css']
})
export class Details implements OnInit{

  id: string | undefined;

  piId!: string;
  sensorId!: string;

  data: any;
  simulated: any;
  time:any;

  loading = true;
  error: string | null = null;
  grafanaUrl: SafeResourceUrl | null = null;
  constructor(
    private cdr: ChangeDetectorRef,
    private route: ActivatedRoute,
    private api: Api,
    private sanitizer: DomSanitizer
  ) {}

  ngOnInit(){

    this.route.paramMap.subscribe(params => {
      this.piId = params.get('piId')!;
      this.sensorId = params.get('sensorId')!;

      this.api.getSensorData(this.piId, this.sensorId).subscribe({
        next: (res: any) => {
          console.log("RESPONSE:", res);
          this.data = res.data;
          this.simulated = res.simulated;
          this.time = new Date(res.time);
          this.loading = false;
          this.grafanaUrl = this.sanitizer.bypassSecurityTrustResourceUrl(
            this.getGrafanaPanelUrl(this.piId,this.sensorId)
          );
          this.cdr.detectChanges();
        },
        error: (err) => {
          console.log("ERROR:", err);
          this.error = "Error loading sensor data";
          this.loading = false;
        }
      });
    });  
  }

  getGrafanaPanelUrl(piId: string,sensorId: string): string {
    if (piId==="pi2" && sensorId==="4sd"){
      return "http://localhost:3000/d-solo/igslgxw/iot-project?orgId=1&from=1771298424483&to=1771320024483&timezone=browser&panelId=panel-9&__feature.dashboardSceneSolo=true";
    }
    else if (piId==="pi2" && sensorId==="dus2"){
      return "http://localhost:3000/d-solo/igslgxw/iot-project?orgId=1&from=1771298424483&to=1771320024483&timezone=browser&panelId=panel-8&__feature.dashboardSceneSolo=true";
    }
    else if (piId==="pi3" && sensorId==="dpir3"){
      return "http://localhost:3000/d-solo/igslgxw/iot-project?orgId=1&from=1771298424483&to=1771320024483&timezone=browser&panelId=panel-7&__feature.dashboardSceneSolo=true";
    }
    else if (piId==="pi2" && sensorId==="dpir2"){
      return "http://localhost:3000/d-solo/igslgxw/iot-project?orgId=1&from=1771298424483&to=1771320024483&timezone=browser&panelId=panel-6&__feature.dashboardSceneSolo=true";
    }
    else if (piId==="pi2" && sensorId==="btn"){
      return "http://localhost:3000/d-solo/igslgxw/iot-project?orgId=1&from=1771298424483&to=1771320024483&timezone=browser&panelId=panel-5&__feature.dashboardSceneSolo=true";
    }
    else if (piId==="pi2" && sensorId==="ds2"){
      return "http://localhost:3000/d-solo/igslgxw/iot-project?orgId=1&from=1771298424483&to=1771320024483&timezone=browser&panelId=panel-4&__feature.dashboardSceneSolo=true";
    }
    else if (piId==="pi1" && sensorId==="ds1"){
      return "http://localhost:3000/d-solo/igslgxw/iot-project?orgId=1&from=1771298424483&to=1771320024483&timezone=browser&panelId=panel-3&__feature.dashboardSceneSolo=true";
    }
    else if (piId==="pi1" && sensorId==="dpir1"){
      return "http://localhost:3000/d-solo/igslgxw/iot-project?orgId=1&from=1771298424483&to=1771320024483&timezone=browser&panelId=panel-2&__feature.dashboardSceneSolo=true";
    }
    else if (piId==="pi1" && sensorId==="dus1"){
      return "http://localhost:3000/d-solo/igslgxw/iot-project?orgId=1&from=1771298424483&to=1771320024483&timezone=browser&panelId=panel-1&__feature.dashboardSceneSolo=true";
    }
    else if(piId=="house" && sensorId==="alarm"){
      return "http://localhost:3000/d-solo/igslgxw/iot-project?orgId=1&from=1771485475665&to=1771507075665&timezone=browser&panelId=panel-10&__feature.dashboardSceneSolo=true";
    }
    else if(piId=="pi1" && sensorId==="db"){
      return "http://localhost:3000/d-solo/igslgxw/odbrana?orgId=1&from=1772170214901&to=1772191814901&timezone=browser&panelId=panel-11&__feature.dashboardSceneSolo=true";
    }
    else if(piId=="pi1" && sensorId==="dl"){
      return "http://localhost:3000/d-solo/igslgxw/odbrana?orgId=1&from=1772170214901&to=1772191814901&timezone=browser&panelId=panel-12&__feature.dashboardSceneSolo=true";
    }
    else if(piId=="pi1" && sensorId==="dms"){
      return "http://localhost:3000/d-solo/igslgxw/odbrana?orgId=1&from=1772170214901&to=1772191814901&timezone=browser&panelId=panel-13&__feature.dashboardSceneSolo=true";
    }
    else if(piId=="pi2" && sensorId==="dht3"){
      return "http://localhost:3000/d-solo/igslgxw/odbrana?orgId=1&from=1772170214901&to=1772191814901&timezone=browser&panelId=panel-14&__feature.dashboardSceneSolo=true";
    }
    else if(piId=="pi2" && sensorId==="gsg"){
      return "http://localhost:3000/d-solo/igslgxw/odbrana?orgId=1&from=1772170214901&to=1772191814901&timezone=browser&panelId=panel-15&__feature.dashboardSceneSolo=true";
    }
    else if(piId=="pi3" && sensorId==="dht1"){
      return "http://localhost:3000/d-solo/igslgxw/odbrana?orgId=1&from=1772170214901&to=1772191814901&timezone=browser&panelId=panel-16&__feature.dashboardSceneSolo=true";
    }
    else if(piId=="pi3" && sensorId==="dth2"){
      return "http://localhost:3000/d-solo/igslgxw/odbrana?orgId=1&from=1772170214901&to=1772191814901&timezone=browser&panelId=panel-17&__feature.dashboardSceneSolo=true";
    }
    else if(piId=="pi3" && sensorId==="ir"){
      return "http://localhost:3000/d-solo/igslgxw/odbrana?orgId=1&from=1772170214901&to=1772191814901&timezone=browser&panelId=panel-18&__feature.dashboardSceneSolo=true";
    }
    else if(piId=="pi3" && sensorId==="brgb"){
      return "http://localhost:3000/d-solo/igslgxw/odbrana?orgId=1&from=1772170214901&to=1772191814901&timezone=browser&panelId=panel-19&__feature.dashboardSceneSolo=true";
    }
    else if(piId=="pi3" && sensorId==="lcd"){
      return "http://localhost:3000/d-solo/igslgxw/odbrana?orgId=1&from=1772170214901&to=1772191814901&timezone=browser&panelId=panel-20&__feature.dashboardSceneSolo=true";
    }
    return "";
  }

}
