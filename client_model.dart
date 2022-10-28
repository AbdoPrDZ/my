import 'package:firebase_database/firebase_database.dart';
import 'package:get/get.dart';
import 'package:storage_database/storage_document.dart';

import '../services/main.service.dart';

class ClientModel {
  final String id;
  String fullname, phone;
  final DateTime createdAt;

  ClientModel(
    this.id,
    this.fullname,
    this.phone,
    this.createdAt,
  );

  static StorageDocument document =
      Get.find<MainService>().storageDatabase.document('data/clients');

  static DatabaseReference ref =
      Get.find<MainService>().firebaseDatabase.ref('clients');

  static Future initListiner() async {
    await document.set((await ref.get()).value ?? {});
    ref.onValue.listen(
      (event) {
        if (event.snapshot.value != null) {
          document.set(event.snapshot.value, keepData: false);
        }
      },
    );
  }

  static Future<ClientModel?> fromId(String id) async {
    Map? data = await document.document(id).get() as Map?;
    return data != null ? fromMap(data) : null;
  }

  static Future<List<ClientModel>> all() async {
    Map? data = await document.get() as Map?;
    return data != null ? allFromMap(data) : [];
  }

  static Stream<List<ClientModel>> stream() =>
      document.stream().asyncExpand<List<ClientModel>>(
        (event) async* {
          if (event != null) {
            Map data = event as Map;
            if (data.isNotEmpty) {
              yield allFromMap(data);
            }
          }
        },
      );

  static List<ClientModel> allFromMap(Map items) =>
      [for (String clientId in items.keys) fromMap(items[clientId])];

  static ClientModel fromMap(Map data) => ClientModel(
        data['id'],
        data['fullname'],
        data['phone'],
        DateTime.fromMillisecondsSinceEpoch(data['created_at']),
      );

  Map<String, dynamic> get map => {
        'id': id,
        'fullname': fullname,
        'phone': phone,
        'created_at': createdAt.millisecondsSinceEpoch,
      };

  static Future<ClientModel> create(ClientModel item) async {
    await ref.child(item.id).set(item.map);
    return item;
  }

  update({String? fullname, String? phone}) async {
    this.fullname = fullname ?? this.fullname;
    this.phone = phone ?? this.phone;
    await ref.child(id).update(map);
  }

  delete() async => remove(id);

  static Future remove(String id) => ref.child(id).remove();
}
