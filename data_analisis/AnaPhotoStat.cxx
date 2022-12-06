#define AnaPhotoStat_cxx
#include "AnaPhotoStat.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

void AnaPhotoStat::Loop()
{
//   In a ROOT session, you can do:
//      root> .L AnaPhotoStat.C
//      root> AnaPhotoStat t
//      root> t.GetEntry(12); // Fill t data members with entry number 12
//      root> t.Show();       // Show values of entry 12
//      root> t.Show(16);     // Read and show values of entry 16
//      root> t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch
   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   curr_evn = 0;
   min1=1;
   min2=1;
   temp_rt=0;
   temp_t=0;
   cnt_t=0;
   delta_t=0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;

      //start analysis code
      
		
      
      if (curr_evn!=evn)
      {
		if (jentry>0)FillData();
		ped0 = 0;
		ped2 = 0;
		signal = 0;
		pulse = 0;
		temp_t=0;
		cnt_ped = 0;
		cnt_signal = 0;
		cnt_pulse = 0;
		min1=1;
		cnt_rt=0;
		temp_t=0;
		cnt_t=0;
		delta_t=0;
		}
      
      ////////////////////////////////////////
      //Asignacion a tipo de pulso 1 o 2
      temp_m =v2;
      if (temp_m<min1){
      	min1=temp_m;   
      }
      if (evn==1){
      	min2=min1;
      }
      
      if ( cnt_rt==0 && temp_m>(min1+0.05) ){
      	return_t[curr_evn]=t;
      	cnt_rt=1;
      }
      
      /////////////////////////////////////////
      //Obtencion delta t
      
      temp_t=t-temp_t;
      delta_t=delta_t+temp_t;
      temp_t=t;
      cnt_t=cnt_t+1;
		
		/////////////////////////////////////////
		//Parte obtencion de lineas base
		 
      if (TMIN_PED0<t&&t<TMAX_PED0)
      {
		ped0+=v0;
		ped2+=v2;
		
      cnt_ped++;
      }
      else if (TMIN_SIGNAL<t&&t<TMAX_SIGNAL)
      {
		signal+=v0;
		cnt_signal++;
      }
      else if (TMIN_PULSE<t&&t<TMAX_PULSE)
      {
		pulse+=v2;
		cnt_pulse++;
      }
      
      //      if(temp_t<t&&)
      //	delta_t+=t-temp_t;

      //hDt->Fill(DT)

      curr_evn=evn;
   }
   
   ////////////////////////////////////
   //Separacion de 2 tipos de onda
   
   min1=1000;
   min2=-10;
  	for(int i=1;i<curr_evn;i++){
  		if(min1>return_t[i]){
  			min1=return_t[i];
  		}
  		if (min2<return_t[i]){
  			min2=return_t[i];
  		}
  	}
  	//cout << min1 << "   " << min2 << "\n"; 
   
   for(int i=1;i<curr_evn;i++){
   	if (return_t[i]==0)
   		cout << i << "\n";
   	if ((min1-time_var)<return_t[i] && return_t[i]<(min1+time_var))
   	{
   		tdata_m1->Fill(QS1[i],QP1[i]);
   		cout << "";
   	}
   	else if ((min2-time_var)<return_t[i] && return_t[i]< (min2+time_var))
   	{
   		tdata_m2->Fill(QS1[i],QP1[i]);
   		cout <<"";
   	}
   }
  
   ofile->Write("",TObject::kOverwrite);
      
}



Int_t AnaPhotoStat::FillData()
{
  Float_t Qs = ped0/cnt_ped*cnt_signal - signal;
  Float_t Qp = ped2/cnt_ped*cnt_pulse - pulse;

  Float_t dt=  delta_t/cnt_t;
  //Qs=Qs*dt
  //Qp=Qp*dt

  tdata_t->Fill(Qs,Qp);
  
  QS1[curr_evn]=Qs;
  QP1[curr_evn]=Qp;
 
  //delta_t=delta_t/(cnt_ped-1);
  //hDt->Fill(delta_t);
  
  return 0;
}
